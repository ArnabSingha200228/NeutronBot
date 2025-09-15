from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import fitz  # PyMuPDF


def process_file(uploaded_file):
    """
    Processes a .txt or .pdf file, generates Gemini-compatible embeddings, and stores in Chroma DB.

    Args:
        uploaded_file: Streamlit uploaded file object
    Returns:
        tokens of file content as Document
    """

    file_name = uploaded_file.name
    file_type = uploaded_file.type
    text = None

    # Extract text
    if file_name.endswith(".txt") or file_type == "text/plain":
        text = uploaded_file.read().decode("utf-8")

    elif file_name.endswith(".pdf") or file_type == "application/pdf":
        pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""
        for page in pdf:
            text += page.get_text()
        if not text.strip():
            st.toast("No text content found in the uploaded file.")
            return None
    else:
        st.toast("Only .txt or .pdf files are supported.")
        return None

    # Split text into chunks and create Document
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = text_splitter.split_text(text)
    if chunks and len(chunks) > 0:
        documents = [Document(page_content=chunk) for chunk in chunks]
        return documents
    else:
        st.toast("Something went wrong, try again later...")
        return None
