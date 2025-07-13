from jinja2 import Template

class TemplateGeneratorAgent:
    def __init__(self, template_str: str):
        self.template = Template(template_str)

    def generate(self, module_name, snippets) -> str:
        return self.template.render(
            module_name=module_name,
            snippets=snippets
        )
