import pandas as pd
from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(df: pd.DataFrame, chunk_size=500, chunk_overlap=100) -> pd.DataFrame:
    """
    Takes a DataFrame with a 'text' column
    and splits text into chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    all_chunks = []

    for _, row in df.iterrows():
        chunks = splitter.split_text(row["text"])

        for chunk in chunks:
            all_chunks.append({
                "page_number": row["page_number"],
                "chunk_text": chunk
            })

    chunk_df = pd.DataFrame(all_chunks)
    return chunk_df


if __name__ == "__main__":
    from pdf_loader import load_pdf

    df = load_pdf("data/raw_pdfs/sample.pdf")
    chunk_df = chunk_text(df)

    print(chunk_df.head())
    print("\nTotal Chunks Created:", len(chunk_df))
