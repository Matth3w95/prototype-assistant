import json
from agents.code_finder import CodeFinderAgent
from agents.template_generator import TemplateGeneratorAgent

def run_new_feature(query: str):
    # 1. Find code snippets
    finder = CodeFinderAgent(index_base="data/code_index")
    snippets = finder.find(query=query, k=3)

    # 2. Load Jinja template
    tpl_str = open("templates/verifier.tpl", encoding="utf8").read()
    templater = TemplateGeneratorAgent(tpl_str)

    # 3. Generate stub
    stub = templater.generate("ProofDslVerifier", snippets)
    return snippets, stub

if __name__ == "__main__":
    import fire
    fire.Fire({"run": run_new_feature})
