from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def load_and_chunk(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    return splitter.split_text(text)

def ingest_folder(folder_path):
    all_chunks = []

    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            chunks = load_and_chunk(os.path.join(folder_path, file))
            all_chunks.extend(chunks)

    return all_chunks
