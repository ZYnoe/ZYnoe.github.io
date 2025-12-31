---
weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
# bookHref: ''
# bookIcon: ''
date: '2025-12-31T00:00:00+09:00'
draft: false
title: 'Elsevier Abstract Downloader'
tags:
- Ontology Tutorial
categories:
- technical
---
# Elsevier Abstract Downloader Walkthrough

I have implemented the Python script `fetch_abstracts.py` to download abstracts from Elsevier Science Direct. It is designed to handle API Rate Limits (Error 429) automatically.

## Prerequisites

You need your **Elsevier API Key**. An **Institutional Token** is recommended for higher rate limits but optional.

## How to Run

1.  **Set Environment Variables**
    Open your terminal and export your keys:
    ```bash
    export ELSEVIER_API_KEY="your_api_key_here"
    # Optional
    export ELSEVIER_INST_TOKEN="your_inst_token_here"
    ```

2.  **Run the Script**
    You can run the script directly with the CSV URL provided:
    ```bash
    python3 fetch_abstracts.py https://raw.githubusercontent.com/M3RG-IITD/MatSciBERT/refs/heads/main/pretraining/piis_dois.csv
    ```

    Or with a local file:
    ```bash
    python3 fetch_abstracts.py local_file.csv
    ```

## Features
- **429 Rate Limit Handling**: Automatically waits and retries if the API limit is reached.
- **Progress Saving**: Saves `abstracts.json` and a `checkpoint.txt` every 10 items. If the script is interrupted, run it again to resume.
- **Output**: Generates `abstracts.json` containing the DOIs and their abstracts.

## Verification
I verified the script logic by running it without keys, confirming it correctly detects the missing configuration.
```text
Error: ELSEVIER_API_KEY environment variable is not set.
```
Once you set the key, it will proceed to download.
