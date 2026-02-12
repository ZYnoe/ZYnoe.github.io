---
title: "What is ontology and semantic memory?"
weight: 1
# bookFlatSection: false
# bookToc: true
# draft: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
# bookHref: ''
# bookIcon: ''
date: "2026-01-27T15:00:56.273Z"
draft: false
tags:
- Ontology Tutorial
categories:
- technical
---


## Is my `.jsonl` dataset a semantic memory dataset?

**Short answer:**  
Yes — your dataset *can* function as a semantic memory dataset, *but it depends on how you define it and how you plan to use it.*

### Clarification

- A **semantic memory dataset** in AI/knowledge systems typically means **structured knowledge that captures meanings, concepts, and relationships**, not just raw text.
- In your case, the `.jsonl` contains **materials properties and characteristics extracted automatically** from 100k peer-reviewed abstracts. That is **structured, factual knowledge about domain concepts**, which is *exactly the kind of data that could serve as semantic memory*.

So your JSONL has:

✔️ Entities (materials, properties)  
✔️ Attributes (values, conditions, evidence)  
✔️ Machine-readable structure

That is *semantic knowledge*, even if it’s not yet a fully conceived ontology with a schema, classes, axioms, logic constraints, etc.

📌 **Conclusion:**  
Your data qualifies as a **semantic knowledge dataset** (like “memory”), but **not yet a full ontology** in the strict sense.

---

## Does what you are doing fit the ontology construction methodology described in the article?

**Short answer:**  
Partially — your current practice overlaps with thematic parts of the methodology, but it is not yet the full methodology as described.

---

### What You *Are* Doing

Your current pipeline:

1. **Text mining** → extract facts from abstracts  
2. Output → `JSONL` with structured fields like:
   - `material`
   - `property`
   - `value`
   - `unit`
   - `condition`
   - `evidence`

This matches **instance extraction** from text — essentially:

> “Concrete facts or triples about real things in the world”  

This is exactly what **instance data** in a semantic knowledge system is supposed to be. It’s the *populated facts* that an ontology can later operate over.

So:

✅ You are building **domain instance data**  
✅ You are extracting structured knowledge from unstructured text  
✅ It *can* support ontology validation and usage  

But…

---

### What the Ontology Methodology Includes (Beyond Instance Extraction)

According to the article’s methodology, an ontology development process includes a **schema layer** and an **instance layer**:

1. **Scenarios & Glossary**  
2. **Competency Questions**  
3. **Modelet Development (schema / classes / properties)**  
4. **Test Case Generation (e.g., SPARQL)**  
5. **Model Refinement**  
6. **Documentation**  
7. **Feedback and iteration**

Your current work focuses on **instance data**, but the methodology emphasizes structuring and refining the **schema first**, *before* you generate and use instance data.

So right now you have:

🔹 **Instance facts only**  
✖️ Not yet a structured domain schema or ontology backbone  
✖️ No competency questions defined formally  
✖️ No test cases derived from ICQs  
✖️ No iterative refinement loop between schema ↔ data

---

## So the answer is

### ❓ Is your JSONL a semantic memory dataset?

➡️ **Yes, in terms of extracted structured data representing domain knowledge.**

### ❓ Is what you are doing the full ontology methodology from the article?

➡️ **Not yet — it covers important parts, but you have done mostly instance extraction, not full ontology engineering.**

---

## How the Two Can Fit Together

Here’s one way to map your workflow into the ontology method:

| Your Current Step                                   | Article Method Step              |
|-----------------------------------------------------|----------------------------------|
| Extract properties from abstracts → JSONL           | **Instance layer**               |
| (Future) Define schemas for materials, properties    | **Modelet / Ontology schema**    |
| Generate competency questions based on domain needs | **ICQs**                         |
| Use ICQs + schema to design tests                   | **Test Case Generation**         |
| Validate your extracted facts against schema & tests | **Refinement**                   |
| Document ontology and iteration results             | **Documentation + Feedback**     |

So your data is **a great foundation** — especially for:

- **Validating ontology**
- **Providing empirical evidence**
- **Feeding test case results**
- **Driving iterative improvement**

---

## Bottom Line

📌 **Your JSONL dataset is semantic knowledge (semantic memory)**  
📌 **Your work is *part* of ontology building, specifically instance extraction**  
📌 **To fully match the methodology, you should add schema, competency questions, test cases, documentation, and iterative feedback**
