---
date: '2025-12-23T20:04:31+09:00'
draft: false
title: '101 Setup'
tags:
- Onotology Tutorial
categories:
- technical
---

## Setup Instructions

In this document, we will guide you through the setup process for the Ontology project.

### Papers to read 

PDFs are available at:
[The Artificial Intelligence Ontology: LLM-assisted](https://github.com/ZYnoe/ZYnoe.github.io/blob/main/content/papers/1.pdf)

### Prerequisites



```python
%pip install --upgrade pip
%pip install pandas
%pip install requests
%pip install bs4
```


```python
import requests
url_nmat = "https://www.nature.com/articles/s41563-023-01620-2"
response = requests.get(url_nmat)
```


```python
print(response)
response.status_code
html = response.text
```


```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
abstract = soup.select_one("#Abs1-content > p")
```


```python
abstract
```


```python
abstract.get_text()
```


```python
def get_abstract(url):
    response = requests.get("https://www.nature.com"+url)
    print(f"Reading abstracts from {url}...")
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        print("Success")
        return soup.select_one('#Abs1-content > p').get_text()
        
    else:
        print(f"Error : {response.status_code}")
        return -1
```


```python
urls_nmat  = ["/articles/s41563-023-01517-0",
"/articles/s41563-023-01572-7",
"/articles/s41563-023-01562-9",
"/articles/s41563-023-01580-7",
"/articles/s41563-023-01550-z",
"/articles/s41563-023-01585-2",
"/articles/s41563-023-01595-0",
"/articles/s41563-023-01560-x",
"/articles/s41563-023-01591-4",
"/articles/s41563-023-01598-x",
"/articles/s41563-023-01584-3",
"/articles/s41563-023-01577-2"]
```


```python
abstracts = [ get_abstract(abstract) for abstract in urls_nmat ]
```


```python
abstracts
```


```python
import pandas as pd
df = pd.DataFrame({
    "url":urls_nmat,
    "abstract":abstracts
})

df.to_csv("extracted_abstracts.csv", index=False)
```
