# agents/template_generator.py

from jinja2 import Template

class TemplateGeneratorAgent:
    """
    Takes a list of snippets and a module name, and renders
    a Jinja2 template stub for your new feature.
    """

    # A simple Jinja stub; extend as needed.
    STUB_TEMPLATE = """
-- Module: {{ module_name }}
-- Generated code stub

{% for snip in snippets %}
-- From: {{ snip['path'] }}
{{ snip['snippet'] | indent(2) }}
{% endfor %}

function {{ module_name }}Verifier() {
  // TODO: implement your verifier logic here
}
"""

    def __init__(self):
        self.template = Template(self.STUB_TEMPLATE)

    def generate(self, module_name, snippets):
        """
        :param module_name: the Haskell (or pseudo) module name for the stub
        :param snippets: list of {"path":…, "snippet":…} dicts
        :return: rendered string
        """
        return self.template.render(
            module_name=module_name,
            snippets=snippets
        )

if __name__ == "__main__":
    import fire
    agent = TemplateGeneratorAgent()
    sample = [{"path": "foo.hs", "snippet": "foo x = x + 1"}]
    print(agent.generate(module_name="MyModule", snippets=sample))
