# agents/code_finder.py

import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class CodeFinderAgent:
    def __init__(self, index_base="data/code_index"):
        # Load vectorizer, paths, and raw docs
        with open(index_base + "_vec.pkl", "rb") as f:
            self.vec, self.paths, self.docs = pickle.load(f)

    def find(self, query: str, k: int = 3):
        # Vectorize query and documents
        qv = self.vec.transform([query])
        dv = self.vec.transform(self.docs)

        # Compute similarities
        sims = cosine_similarity(qv, dv).flatten()

        # Get top-k indices
        idxs = np.argsort(-sims)[:k]

        # Return path and snippet
        return [
            {
                "path": self.paths[i],
                "snippet": self.docs[i][:500],
            }
            for i in idxs
        ]


if __name__ == "__main__":
    agent = CodeFinderAgent()
    results = agent.find(
        query="proof-dsl tagless-final example",
        k=3,
    )
    print(results)
