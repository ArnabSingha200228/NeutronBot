import uuid
import streamlit as st

def store_embeddings(
    documents,
    source,
    embedding_model=None,
    collection_name="file_embeddings",
):
    """
        Generates the embeddings of tokens and stores in chroma db

        Args:
            documents : Langchain Documents containing tokens
            source : source for assigning metadata
            embedding_model : Used embedding model
            collection_name : name of the collection to be given
        Returns:
            tokens of file content as Document
    """


    # Step 3: Initialize Gemini-compatible embedding model
    embedding_model = embedding_model

    # Step 5: Initialize Chroma client and collection
    client = st.session_state["client"]
    collection = None
    try:
        collection = client.get_collection(name=collection_name)
    except:
        collection = client.create_collection(name=collection_name)

    # Step 6: Add documents to Chroma with embeddings
    try:
        embeddings = embedding_model.embed_documents(
            [doc.page_content for doc in documents]
        )
        collection.add(
            documents=[doc.page_content for doc in documents],
            metadatas=[{"source": source}] * len(documents),
            ids=[f"{source}_{i}_{uuid.uuid4().hex}" for i in range(len(documents))],
            embeddings=embeddings,
        )
    except:
        return "Could not get resource..."
    return f"Successfully processed and stored the resource."
