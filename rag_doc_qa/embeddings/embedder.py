import pandas as pd
import numpy as np
import faiss
import os
import pickle
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"

VECTOR_STORE_PATH = "vector_store"
INDEX_FILE = os.path.join(VECTOR_STORE_PATH, "faiss_index.index")
METADATA_FILE = os.path.join(VECTOR_STORE_PATH, "chunks.pkl")


def generate_embeddings(chunk_df: pd.DataFrame):
    model = SentenceTransformer(MODEL_NAME)
    texts = chunk_df["chunk_text"].tolist()
    embeddings = model.encode(texts, show_progress_bar=True)
    return embeddings


def create_faiss_index(embeddings: np.ndarray):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
    return index


if __name__ == "__main__":
    from ingestion.pdf_loader import load_pdf
    from ingestion.text_chunker import chunk_text

    os.makedirs(VECTOR_STORE_PATH, exist_ok=True)

    # Load & chunk
    df = load_pdf("data/raw_pdfs/sample.pdf")
    chunk_df = chunk_text(df)

    # Embed
    embeddings = generate_embeddings(chunk_df)

    # Create index
    index = create_faiss_index(embeddings)

    # Save index
    faiss.write_index(index, INDEX_FILE)

    # Save metadata (chunks)
    with open(METADATA_FILE, "wb") as f:
        pickle.dump(chunk_df, f)

    print("✅ FAISS index saved.")
    print("✅ Chunk metadata saved.")
    print("Total vectors:", index.ntotal)
    print("Vector dimension:", index.d)