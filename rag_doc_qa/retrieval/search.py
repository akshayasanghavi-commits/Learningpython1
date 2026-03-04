import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"
INDEX_FILE = "vector_store/faiss_index.index"
METADATA_FILE = "vector_store/chunks.pkl"


class DocumentSearcher:
    def __init__(self):
        self.model = SentenceTransformer(MODEL_NAME)
        self.index = faiss.read_index(INDEX_FILE)

        with open(METADATA_FILE, "rb") as f:
            self.chunk_df = pickle.load(f)

    def search(self, query, top_k=3):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_embedding), top_k)

        results = []
        for idx in indices[0]:
            results.append(self.chunk_df.iloc[idx]["chunk_text"])

        return results


if __name__ == "__main__":
    searcher = DocumentSearcher()

    query = input("Enter your question: ")

    results = searcher.search(query)

    print("\nTop Matching Chunks:\n")
    for i, res in enumerate(results, 1):
        print(f"Result {i}:\n{res}\n")
