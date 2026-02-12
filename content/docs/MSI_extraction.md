---
title: "Materials Science Information Extraction Documentation"
weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
# bookHref: ''
# bookIcon: ''
date: "2026-02-11T04:49:53+00:00"
draft: false
tags:
- Materials Science
- Information Extraction
- Data Extraction
- Tutorial
- Parallel Processing
categories:
- technical
- tutorial
---

# [langextract](https://github.com/google/langextract)
This code uses ```langextract``` to automatically extract structured information from materials science research abstracts using a local LLM (Gemma 3 12B via Ollama).



## What This Code Does
The script processes research abstracts and extracts key information including material compositions, synthesis methods, characterization techniques, quantitative parameters, and applications. It outputs results as both a JSONL file and an HTML visualization.

## Core Workflow

The extraction process follows four main steps:

- Define extraction rules - Specify what types of information to extract and how to structure it

- Provide training examples - Show the model what good extractions look like

- Process abstracts - Run the extraction on your dataset

- Save and visualize - Export results in structured format and generate HTML visualization


## How to Modify the Code

### Changing What Gets Extracted

Modify the ```extraction_class``` values in the ```examples``` list to extract different types of information. Current classes are:

- `material_composition` - Chemical formulas and material descriptions
- `synthesis_method` - Fabrication and preparation techniques
- `characterization_technique` - Analytical methods (XRD, TEM, etc.)
- `quantitative_parameter` - Numerical measurements with units

**To add new extraction classes:**

```python
lx.data.Extraction(
    extraction_class="your_new_class",  # e.g., "optical_property"
    extraction_text="exact text from abstract",
    attributes={
        "key1": "value1",  # Add relevant attributes
        "key2": "value2"
    }
)
```
### Adjusting the Extraction Prompt

Edit the ```prompt``` variable to focus on different aspects:

```python
prompt = textwrap.dedent("""\
    Extract information about [YOUR FOCUS AREA].
Focus on: [specific items you want], [additional details], 
[formatting preferences].
Use exact text from the original.""")
```

