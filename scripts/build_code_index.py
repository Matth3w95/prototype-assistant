# scripts/build_code_index.py
# scripts/build_code_index.py

import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

def load_files(root_dir, exts=(".hs",".py",".js",".ts")):
    for subdir, _, files in os.walk(root_dir):
        for f in files:
            if f.endswith(exts):
                path = os.path.join(subdir, f)
                with open(path, encoding="utf8", errors="ignore") as fh:
                    yield path, fh.read()

def build_index(repo_path: str, index_path: str):
    # Load all files
    paths, docs = zip(*list(load_files(repo_path)))
    # Fit TF-IDF
    vec = TfidfVectorizer(max_features=5000)
    tfidf_matrix = vec.fit_transform(docs)
    # Persist vectorizer + data
    with open(index_path + "_vec.pkl", "wb") as f:
        pickle.dump((vec, paths, docs), f)
    print(f"Index built: {len(paths)} documents.")

if __name__=="__main__":
    import sys
    build_index(sys.argv[1], sys.argv[2])
