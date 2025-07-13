-- {{ module_name }}.hs
module {{ module_name }} where

{% for s in snippets -%}
-- From {{ s.path }}
{{ s.snippet }}
{% endfor %}

-- | Your verifier stub
verify :: IO ()
verify = putStrLn "TODO: implement"
