import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

def load_files(root_dir, exts=(".hs", ".py", ".js", ".ts")):
    for subdir, _, files in os.walk(root_dir):
        for f in files:
            if f.endswith(exts):
                path = os.path.join(subdir, f)
                with open(path, encoding="utf8", errors="ignore") as fh:
                    yield path, fh.read()

if __name__ == "__main__":
    repo_path = "."
    data = list(load_files(repo_path))
    paths, docs = zip(*data)
    vectorizer = TfidfVectorizer()
    vec = vectorizer.fit(docs)
    with open("data/code_index_vec.pkl", "wb") as f:
        pickle.dump((vectorizer, paths, docs), f)
    print("Index built")
