import pytest
from agents.template_generator import TemplateGeneratorAgent

def test_template_renders_module_name_and_no_snippets():
    tpl = "-- {{ module_name }}\n{% for s in snippets %}X{% endfor %}"
    agent = TemplateGeneratorAgent(tpl)
    out = agent.generate("MyMod", [])
    assert "-- MyMod" in out
    assert "X" not in out

def test_template_includes_snippet_content():
    tpl = "-- header\n{% for s in snippets %}/*{{ s.snippet }}*/{% endfor %}"
    agent = TemplateGeneratorAgent(tpl)
    sample = [{"path": "foo", "snippet": "bar"}]
    out = agent.generate("Any", sample)
    assert "/*bar*/" in out

@pytest.mark.parametrize("snippets,expected", [
    ([], "-- FooModule"),
    ([{"path": "a.hs","snippet": "foo = 1"}], "-- From a.hs\nfoo = 1"),
])
def test_generate_with_parametrized_inputs(snippets, expected):
    tpl = "-- {{ module_name }}\n" \
          "{% for s in snippets %}-- From {{ s.path }}\n" \
          "{{ s.snippet }}\n{% endfor %}"
    agent = TemplateGeneratorAgent(tpl)
    out = agent.generate("FooModule", snippets)
    assert expected in out
