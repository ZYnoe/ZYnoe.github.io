import langextract as lx  
from langextract import io  
  
documents = list(io.load_annotated_documents_jsonl("extraction_results.jsonl"))  
  
# Create individual visualizations  
for i, doc in enumerate(documents):  
    html_content = lx.visualize(doc)  
    with open(f"visualization_doc_{i}.html", "w", encoding='utf-8') as f:  
        f.write(html_content)

import os  
import glob  
  
html_files = glob.glob("visualization_doc_*.html")  
html_files.sort()  
  
combined_html = """<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <meta name="viewport" content="width=device-width, initial-scale=1.0">  
    <title>Combined LangExtract Visualizations</title>  
    <style>  
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; }  
        .nav {   
            position: fixed;   
            top: 0;   
            left: 0;   
            width: 200px;   
            height: 100vh;   
            background: #f5f5f5;   
            padding: 20px;   
            overflow-y: auto;   
            border-right: 1px solid #ddd;  
        }  
        .content {   
            margin-left: 220px;   
            height: 100vh;  
        }  
        .nav-item {   
            cursor: pointer;   
            padding: 8px 12px;   
            margin: 2px 0;   
            border-radius: 4px;   
            background: white;   
            border: 1px solid #ddd;  
        }  
        .nav-item:hover {   
            background: #e0e0e0;   
        }  
        .nav-item.active {   
            background: #007bff;   
            color: white;   
        }  
        iframe {  
            width: 100%;  
            height: 100vh;  
            border: none;  
        }  
    </style>  
</head>  
<body>  
    <div class="nav">  
        <h3>Documents</h3>  
"""  
  
# Add navigation  
for i, html_file in enumerate(html_files):  
    doc_num = html_file.split('_')[-1].replace('.html', '')  
    combined_html += f'        <div class="nav-item" onclick="showDoc({i}, \'{html_file}\')">Document {doc_num}</div>\n'  
  
combined_html += """    </div>  
    <div class="content">  
        <iframe id="docFrame" src=""></iframe>  
    </div>  
  
    <script>  
        function showDoc(docIndex, filename) {  
            // Update active nav item  
            const navItems = document.querySelectorAll('.nav-item');  
            navItems.forEach(item => item.classList.remove('active'));  
            navItems[docIndex].classList.add('active');  
              
            // Load document in iframe  
            document.getElementById('docFrame').src = filename;  
        }  
          
        // Show first document by default  
        showDoc(0, '""" + html_files[0] + """');  
    </script>  
</body>  
</html>"""  
  
with open("combined_visualizations_iframe.html", "w", encoding='utf-8') as f:  
    f.write(combined_html)
