\# Prototype Engineer Assistant



This repository demonstrates a minimal “New Feature Kick-Off” pipeline:

1\. \*\*Index your code\*\* with TF-IDF (`scripts/build\_code\_index.py`).  

2\. \*\*Find relevant snippets\*\* and \*\*generate a Haskell stub\*\* via Jinja2 templates.  

3\. \*\*(CI)\*\* On every push/PR, GitHub Actions runs your Python pipeline automatically.



\## Local Usage



```bash

\# Install dependencies

pip install scikit-learn jinja2 fire



\# Build the code index (only needs doing when code changes)

python scripts/build\_code\_index.py . data/code\_index



\# Run the pipeline with your query

python -m pipeline.new\_feature run --query "proof-dsl tagless-final example"



