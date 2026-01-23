---
title: "langextract_concurrent.py Tutorial"
weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
# bookHref: ''
# bookIcon: ''
date: "2026-01-23T04:49:53+00:00"
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
# langextract_concurrent.py Tutorial

This tutorial explains how to run and understand `concurrent_demo.py`, a small demo that extracts structured materials-science data from research abstracts using multiple concurrent model instances.

## What the script does
- Loads abstracts from `abstracts.json`.
- Uses a prompt and a high-quality example to guide extraction.
- Runs multiple Ollama model instances in parallel using `ThreadPoolExecutor`.
- Saves structured results to `extraction_results.jsonl`.
- Generates a visual HTML report in `visualization.html`.

## Prerequisites
1. Python environment with the required packages installed (notably `langextract` and its dependencies).
```bash
pixi install
```
2. An Ollama server running locally at `http://localhost:11434`.
```bash
export OLLAMA_NUM_PARALLEL=num_worker
```
3. The `gemma3:12b` model pulled in Ollama.
4. Input file `abstracts.json` present in the same folder.

## Files used and produced
- Input: `abstracts.json`
- Output: `extraction_results.jsonl`
- Output: `visualization.html`

## Quick start
From the project directory:

```bash
python langextract_concurrent.py
```

You should see progress messages like:

```text
Completed abstract 1/10
Completed abstract 2/10
...
Runtime: 
```

## How the script is organized
1. **Prompt + example**: A detailed prompt and a labeled example guide the model to extract specific fields.
2. **Data load**: Reads `abstracts.json` and collects the first 10 abstracts.
3. **Parallel execution**:
   - Creates multiple `OllamaLanguageModel` instances.
   - Submits extraction tasks to a thread pool.
4. **Saving + visualization**:
   - Writes results to a JSONL file.
   - Creates an HTML visualization for inspection.

## Key settings you can change
- **Number of workers**: Increase or decrease `num_workers` depending on your CPU/GPU resources.
- **Model**: Change `model_id` to a different Ollama model you have installed.
- **Abstract count**: Change `demo_abstracts = abstracts[:10]` to process more or fewer items.
- **Chunk size**: Adjust `max_char_buffer` if your abstracts are longer or shorter.

## Tips
- Start with `num_workers = 1` to confirm everything works, then scale up.
- If you see timeouts, increase `timeout` in the model config.
- If output is empty or low quality, refine the prompt or add more example extractions.

## Troubleshooting
- **Ollama not running**: Start it and verify the URL and port.
- **Model not found**: Run `ollama pull gemma3:12b`.
- **Empty outputs**: Check `abstracts.json` has a non-empty `abstract` field for each item.
- **Slow runs**: Reduce `num_workers`, or use a smaller model.

## What to look at next
- Review the structured output in `extraction_results.jsonl`.
- Open `visualization.html` in a browser to inspect the extraction highlights.
