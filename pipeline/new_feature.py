# pipeline/new_feature.py

import json
from agents.code_finder import CodeFinderAgent
from agents.template_generator import TemplateGeneratorAgent
import fire

def run_new_feature(query: str):
    # 1. Find code snippets
    finder = CodeFinderAgent(index_base="data/code_index")
    snippets = finder.find(query=query, k=3)

    # 2. Print snippets
    print("=== Found Snippets ===")
    print(json.dumps(snippets, indent=2))

    # 3. Instantiate code stub with **those** snippets
    templater = TemplateGeneratorAgent()
    stub = templater.generate(
        module_name="ProofDslVerifier",  # pick your module name
        snippets=snippets               # pass in the real snippets!
    )
    print("\n=== Generated Stub ===\n")
    print(stub)

if __name__ == "__main__":
    fire.Fire({"run": run_new_feature})
