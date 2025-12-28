---
date: '2025-12-28T22:07:33+09:00'
draft: false
title: 'What is Ontology'
tags:
- Ontology Tutorial
categories:
- technical
---
# What is Ontology? (my understanding)

How can structured concepts and relationships be distilled from unstructured data or fragmented resources to enable interoperability and retrieval?

Ontology’s value proposition is that it turns fragmented/unstructured information into interoperable and searchable structured knowledge, typically by serving as the shared semantic “schema” for data integration and querying across systems.



## Correspondence to the papers

- Turning unstructured data or fragmented resources into structured concepts and relationships corresponds to the ontology learning / ontology construction workflow (term extraction, term typing, taxonomy construction, relation extraction, and axiom discovery), whose goal is to transform text and similar inputs into computable concepts, hierarchies, and relations [3](https://github.com/ZYnoe/ZYnoe.github.io/blob/main/content/papers/3.pdf).

- Ontologies are often described as a semantic layer that standardizes domain concepts and the relations among them, so different databases/tools/formats can “mean the same thing” even if they store data differently, which enables semantic interoperability and supports cross-source retrieval, integration, and reasoning [4](https://github.com/ZYnoe/ZYnoe.github.io/blob/main/content/papers/4.pdf) [5](https://github.com/ZYnoe/ZYnoe.github.io/blob/main/content/papers/5.pdf) [6](https://github.com/ZYnoe/ZYnoe.github.io/blob/main/content/papers/6.pdf).

- An ontology is not only about “distilling structure from unstructured data”; it is a reusable semantic framework that formally captures a domain’s meaning. It uses classes, properties, and relations to provide machine-actionable definitions in formal languages such as RDF and OWL, thereby enabling automated reasoning and consistency checking [4](https://github.com/ZYnoe/ZYnoe.github.io/blob/main/content/papers/4.pdf) [5](https://github.com/ZYnoe/ZYnoe.github.io/blob/main/content/papers/5.pdf).

- For example, work in the materials domain explicitly positions an ontology as a shared, extensible model for data exchange, reuse, and integration, and as a semantic mapping layer that resolves mismatches in terminology and structure across heterogeneous databases [4](https://github.com/ZYnoe/ZYnoe.github.io/blob/main/content/papers/4.pdf).

# Engineering approach of Ontology
