import csv
import os
import requests
import time
import argparse
import json
from datetime import datetime

# Constants
API_URL_TEMPLATE = "https://api.elsevier.com/content/article/doi/{}"
HEADERS = {
    "Accept": "application/json",
    "X-ELS-APIKey": os.environ.get("ELSEVIER_API_KEY", ""),
    "X-ELS-Insttoken": os.environ.get("ELSEVIER_INST_TOKEN", "")
}
OUTPUT_FILE = "abstracts.json"
CHECKPOINT_FILE = "checkpoint.txt"

def get_doi_abstract(doi):
    """
    Fetches the abstract for a given DOI from Elsevier API.
    Handles rate limiting (429) and other errors.
    """
    url = API_URL_TEMPLATE.format(doi)
    
    # Simple Exponential Backoff
    delay = 1
    max_retries = 5
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=HEADERS)
            
            if response.status_code == 200:
                data = response.json()
                try:
                    # Navigate the complex JSON structure to find the abstract
                    # Structure varies, but usually: 'full-text-retrieval-response' -> 'coredata' -> 'dc:description'
                    # OR 'abstracts' section.
                    # For basic metadata/abstract, 'coredata' often has 'dc:description' which is the abstract.
                    
                    # Common path for abstract in Article Retrieval API
                    coredata = data.get('full-text-retrieval-response', {}).get('coredata', {})
                    abstract = coredata.get('dc:description', "")
                    
                    if not abstract:
                        # Fallback check
                        abstract = "No abstract found in response"
                        
                    return {"doi": doi, "abstract": abstract, "status": "success"}
                    
                except Exception as e:
                    return {"doi": doi, "error": f"Parsing error: {str(e)}", "status": "failed"}

            elif response.status_code == 429:
                # Rate Limited
                retry_after = response.headers.get("Retry-After")
                if retry_after:
                    wait_time = int(retry_after) + 1
                else:
                    wait_time = delay
                
                print(f"Rate limit hit for {doi}. Waiting {wait_time}s...")
                time.sleep(wait_time)
                delay *= 2 # Exponential backoff for next time if header is missing
                continue
                
            elif response.status_code == 404:
                 return {"doi": doi, "error": "DOI not found (404)", "status": "failed"}
            
            else:
                return {"doi": doi, "error": f"HTTP {response.status_code}", "status": "failed"}
                
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            time.sleep(delay)
            delay *= 2
            
    return {"doi": doi, "error": "Max retries exceeded", "status": "failed"}

def process_dois(input_csv):
    """
    Reads DOIs from CSV and fetches abstracts.
    """
    if not HEADERS["X-ELS-APIKey"]:
        print("Error: ELSEVIER_API_KEY environment variable is not set.")
        return

    dois = []
    # Handle URL input or local file
    if input_csv.startswith("http"):
        print(f"Downloading CSV from {input_csv}...")
        r = requests.get(input_csv)
        if r.status_code != 200:
            print("Failed to download CSV.")
            return
        decoded_content = r.content.decode('utf-8')
        reader = csv.DictReader(decoded_content.splitlines())
    elif os.path.exists(input_csv):
        with open(input_csv, 'r') as f:
            reader = csv.DictReader(f)
    else:
        print(f"Error: File {input_csv} not found.")
        return
    
    # Determine the column name for DOI
    # The snippet showed 'DOI' as a column header
    # We need to handle the iterator correctly if it's a file vs list
    # csv.DictReader is an iterator.
    
    # We need to iterate once to extract DOIs
    try:
        # Check fieldnames if possible to be robust
        if reader.fieldnames:
            print(f"CSV Columns: {reader.fieldnames}")
            
        for row in reader:
            if 'DOI' in row:
                dois.append(row['DOI'])
            elif 'doi' in row:
                 dois.append(row['doi'])
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return
    
    print(f"Found {len(dois)} DOIs to process.")
    
    # Load checkpoint if exists
    start_index = 0
    if os.path.exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE, 'r') as f:
             try:
                start_index = int(f.read().strip())
             except:
                start_index = 0
        print(f"Resuming from index {start_index}")

    results = []
    # Load existing results if resuming
    if start_index > 0 and os.path.exists(OUTPUT_FILE):
         with open(OUTPUT_FILE, 'r') as f:
            try:
                results = json.load(f)
            except:
                results = []

    for i in range(start_index, len(dois)):
        doi = dois[i]
        print(f"Processing ({i+1}/{len(dois)}): {doi}")
        
        result = get_doi_abstract(doi)
        results.append(result)
        
        # Save progress every 10 requests
        if i % 10 == 0:
            with open(OUTPUT_FILE, 'w') as f:
                json.dump(results, f, indent=2)
            with open(CHECKPOINT_FILE, 'w') as f:
                f.write(str(i + 1))
        
        # Be nice to the API
        time.sleep(0.5) 

    # Final save
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Cleanup checkpoint on success
    if os.path.exists(CHECKPOINT_FILE):
        os.remove(CHECKPOINT_FILE)
        
    print("Done! Results saved to", OUTPUT_FILE)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download abstracts from Elsevier")
    parser.add_argument("csv_path", help="Path or URL to the CSV file containing DOIs")
    args = parser.parse_args()
    
    process_dois(args.csv_path)
