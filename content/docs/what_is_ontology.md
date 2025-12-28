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

## Engineering approach of Ontology

Computational materials ontology engineering approaches are usually not about a single “uniquely correct method.” Instead, an approach is chosen around the target use cases (competency questions), the form of the data sources (computational workflows/databases/literature), and interoperability requirements. Below is a practical summary of the most common engineering routes (each corresponding to typical representative works/frameworks) [(Aameri et al., 2023).](https://journals.sagepub.com/doi/full/10.3233/SW-233340)

### [Upper-ontology alignment + modular ontology](https://www.nature.com/articles/s41597-025-04938-5) (I need to revise it because I’m still confused)

The paper outlines simple, practical methods for MDS-Onto to align with upper ontologies and build modular ontologies. These approaches make the ontology flexible and compatible with broader standards.
​
#### Upper Ontology Alignment
MDS-Onto, a domain-specific ontology, connects to top-level ontologies like BFO (Basic Formal Ontology) using mid-level bridges such as PMDco and PROV-O. The steps involve mapping core terms (e.g., "material" or "process") to BFO's basic categories (e.g., "continuant" for enduring things and "occurrent" for events), linking materials science concepts via PMDco for semantic sharing, and adding Schema.org plus PROV-O for web compatibility and early term conflict resolution.


#### Modular Ontology Design
MDS-Onto uses a layered setup with a top core module for shared terms and subdomain modules (e.g., X-ray or photovoltaics). Subdomains reuse top terms and add specifics (like "bandgap" for photovoltaics), keeping changes isolated; tools like FAIRmaterials help experts build and merge interoperable modules without direct dependencies, ensuring easy updates and consistency.

### [Schema-first / API-first](https://link.springer.com/chapter/10.1007/978-3-030-62466-8_14)

Schema-first is an ontology development approach in which you first define a data schema (e.g., OPTIMADE’s standardized field definitions) and then build the ontology’s concepts and relations on top of that schema, ensuring the ontology stays aligned with existing database structures.

Think of it like building a house: a data-first approach is like piling up materials and only then trying to design the blueprint—things can end up unstable. A schema-first approach draws the blueprint (the schema) first and then builds accordingly, so data from different databases can connect seamlessly.

In the paper’s development of the Materials Design Ontology (MDO), the authors follow the NeOn methodology scenario of “reusing non-ontological resources” by extracting terms from the OPTIMADE schema (a consensus data model). These terms guide the definition of concepts such as “structure,” “calculation,” and “property,” avoiding the need to start from messy raw data.

As a result, MDO can map data from resources like the Materials Project into RDF and support SPARQL queries (e.g., finding materials with a band gap > 5 eV), enabling interoperability across heterogeneous databases and aligning with the FAIR principles

### [Process-structure-property (PSP)](https://arxiv.org/pdf/2211.10407)

This paragraph is intentionally left blank


### [lightweight ontology](https://arxiv.org/pdf/2412.17877)

This paragraph is intentionally left blank

### Semi-automated / automated ontology engineering (text mining, topic modeling, LLM-assisted).

[LLM-supported collaborative ontology design for data and knowledge management platforms](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1676477/full)

[HIVE-4-MAT: Advancing the Ontology Infrastructure for Materials Science](https://link.springer.com/chapter/10.1007/978-3-030-71903-6_28)