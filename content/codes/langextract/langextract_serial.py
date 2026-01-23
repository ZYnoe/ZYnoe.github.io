import langextract as lx
import textwrap
import json
import time

start = time.perf_counter()
# 1. Define the prompt and extraction rules
prompt = textwrap.dedent("""\
    Extract materials science information from research abstracts.
    Focus on: material compositions with chemical formulas, synthesis methods, 
    characterization techniques with abbreviations, quantitative parameters with values and units, 
    performance improvements with before/after comparisons, and potential applications.
    Use exact text from the original. Provide detailed attributes for scientific context.""")

# 2. Provide a high-quality example to guide the model
examples = [
    lx.data.ExampleData(
        text="""A Nd3+-doped transparent oxyfluoride glass ceramic containing Sr5(PO4)3F nanocrystals was prepared by melt quenching technique and subsequent thermal treatment. 
        The phase and morphology of Sr5(PO4)3F nanocrystals were investigated by X-ray diffraction and transmission electron microscopy, respectively. 
        The volume fraction of Sr5(PO4)3F nanocrystals in the glass ceramic is about 12% and the fraction of Nd3+ ions incorporated in the Sr5(PO4)3F nanocrystals is about 15%.""",
        extractions=[
            lx.data.Extraction(
                extraction_class="material_composition",
                extraction_text="Nd3+-doped transparent oxyfluoride glass ceramic",
                attributes={
                    "dopant": "Nd3+",
                    "matrix": "oxyfluoride glass ceramic",
                    "property": "transparent"
                    }
            ),
            lx.data.Extraction(
                extraction_class="material_composition",
                extraction_text="Sr5(PO4)3F nanocrystals",
                attributes={
                    "chemical_formula": "Sr5(PO4)3F",
                    "morphology": "nanocrystals"
                    }
            ),
            lx.data.Extraction(
                extraction_class="synthesis_method",
                extraction_text="melt quenching technique and subsequent thermal treatment",
                attributes={
                    "primary_method": "melt quenching",
                    "secondary_process": "thermal treatment",
                    "sequence": "two-step"}
            ),
            lx.data.Extraction(
                extraction_class="characterization_technique",
                extraction_text="X-ray diffraction",
                attributes={
                    "abbreviation": "XRD",
                    "purpose": "phase investigation"
                    }
            ),
            lx.data.Extraction(
                extraction_class="characterization_technique",
                extraction_text="transmission electron microscopy",
                attributes={
                    "abbreviation": "TEM",
                    "purpose": "morphology"
                    }
            ),
            lx.data.Extraction(
                extraction_class="quantitative_parameter",
                extraction_text="fraction of Nd3+ ions incorporated in the Sr5(PO4)3F nanocrystals is about 15%",
                attributes={
                    "parameter_type": "incorporation fraction",
                    "value": "15",
                    "unit": "%",
                    "species": "Nd3+ ions",
                    "host": "Sr5(PO4)3F nanocrystals"
                    }
            ),
        ]
    )
]

# The input text to be processed

with open('abstracts.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    
    # extract abstract
    abstracts = [
        item['abstract'].strip() 
        for item in data 
        if item.get('abstract')
    ]
    
# print(f"Loaded {len(abstracts)} abstracts.")
# print("Processing the first 2 abstracts...")

demo_abstracts = abstracts[:10]

results = []
for abstract in demo_abstracts:
    abstract = abstract.replace('\n', ' ')
    # Run the extraction
    result = lx.extract(
        text_or_documents=abstract,
        prompt_description=prompt,
        examples=examples,
        model_id="gemma3:12b",  # Automatically selects Ollama provider
        model_url="http://localhost:11434",
        fence_output=False,
        max_workers=2,
        use_schema_constraints=False,
        max_char_buffer=1000
    )
    results.append(result)


# Save the results to a JSONL file
lx.io.save_annotated_documents(results, output_name="extraction_results.jsonl", output_dir=".")

# Generate the visualization from the file
html_content = lx.visualize("extraction_results.jsonl")
with open("visualization.html", "w", encoding='utf-8') as f:
    if hasattr(html_content, 'data'):
        f.write(html_content.data)  # For Jupyter/Colab
    else:
        f.write(html_content)

end = time.perf_counter()
print(f"Runtime: {end - start:.6f} seconds")