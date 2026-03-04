from pypdf import PdfReader
import pandas as pd
import os


def load_pdf(file_path: str) -> pd.DataFrame:
    """
    Loads a PDF file and returns a Pandas DataFrame
    with page number and extracted text.
    """
    reader = PdfReader(file_path)
    pages_data = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        pages_data.append({
            "page_number": page_number,
            "text": text
        })

    df = pd.DataFrame(pages_data)
    return df


if __name__ == "__main__":
    # Example test run
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    sample_path = os.path.join(project_dir, "data", "raw_pdfs", "sample.pdf")
    print(f"Loading PDF from: {sample_path}")
    if os.path.exists(sample_path):
        df = load_pdf(sample_path)
        print(df.head())
    else:
        print(f"File not found: {sample_path}")
        print("Place a PDF named 'sample.pdf' inside data/raw_pdfs/")
