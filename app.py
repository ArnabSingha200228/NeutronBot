import streamlit as st
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage
import chromadb
from chatmodule.embedder import *
from chatmodule.utils import *
from chatmodule.urlprocessor import *
from chatmodule.fileprocessor import *
from designmodule.design import *
import yaml

load_dotenv()
with open("conf.yaml", "r") as f:
    config = yaml.safe_load(f)


st.set_page_config(page_title="Neutron☄️⭐🌟🌍👽🤖☄", page_icon="🤖")
# custom css
st.markdown(typing_indicator_animation, unsafe_allow_html=True)

persist_directory = config["VECTOR_DB_PERSIS_DIR"]

ensure_event_loop()  # <-- ensure loop exists

if "embedding_model" not in st.session_state:
    st.session_state["embedding_model"] = GoogleGenerativeAIEmbeddings(
        model=config["EMBEDDING_MODEL"]
    )

if "chat_model" not in st.session_state:
    st.session_state["chat_model"] = ChatGoogleGenerativeAI(model=config["CHAT_MODEL"])

if "client" not in st.session_state:
    st.session_state["client"] = chromadb.PersistentClient(path=persist_directory)


def main():

    model = st.session_state["chat_model"]

    if "uploaded_files" not in st.session_state:
        st.session_state.uploaded_files = []  # list of dicts with {name, data, type}

    # Sidebar: Upload + file list
    st.sidebar.markdown(headr, True)
    st.sidebar.header("File Panel")

    if "uploader_key" not in st.session_state:
        st.session_state.uploader_key = 0

    uploaded_file = st.sidebar.file_uploader(
        "Upload a file",
        type=["pdf", "txt"],
        key=st.session_state.uploader_key,
    )

    # Save uploaded file into session state
    if uploaded_file is not None:
        documents = process_file(uploaded_file)
        if documents:
            st.toast(
                store_embeddings(
                    documents,
                    uploaded_file.name,
                    embedding_model=st.session_state["embedding_model"],
                )
            )
            file_info = {
                "name": uploaded_file.name,
                "type": uploaded_file.type,
            }
            st.session_state.uploaded_files.append(file_info)
            st.sidebar.success(f"Uploaded {uploaded_file.name}")
            uploaded_file = None
            st.session_state.uploader_key += 1

        else:
            st.toast("Failed to upload file...")

    # Show uploaded files
    if st.session_state.uploaded_files:
        st.sidebar.subheader("Uploaded Files")
        for f in st.session_state.uploaded_files:
            st.sidebar.text(f["name"])

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state["messages"] = []
        st.markdown(headr, True)
        st.markdown("""##### 🙋‍♂️ Hey there! Let's start.""")
    else:
        st.markdown(headr, True)

    if "started" not in st.session_state:
        st.markdown(instructions, unsafe_allow_html=True)

    for msg in st.session_state["messages"]:
        if msg["role"] == "user":
            if is_url(msg["content"]):
                st.success(f'You provided a [link]({msg["content"]})')

            else:
                st.chat_message("user").write(msg["content"])
        else:
            st.chat_message("assistant").write(msg["content"])

    if msgg := st.chat_input("Type your message or paste an web URL..."):
        if is_url(msgg):
            documents = process_url(msgg)
            if documents:
                st.toast(
                    store_embeddings(
                        documents,
                        "web",
                        collection_name="web_embeddings",
                        embedding_model=st.session_state["embedding_model"],
                    )
                )
                st.session_state["messages"].append({"role": "user", "content": msgg})
                st.success(f"You provided a [link]({msgg})")
        # print(msgg)
        elif (
            msgg[0 : len("File:")].lower() == "file:"
            or msgg[0 : len("Web:")].lower() == "web:"
        ):

            def chroma_retriever(
                query,
                coll_name="file_embeddings",
                top_k=5,
                embedding_model=st.session_state["embedding_model"],
            ):
                client = st.session_state["client"]
                collection = client.get_collection(name=coll_name)
                query_emb = embedding_model.embed_query(query)
                results = collection.query(
                    query_embeddings=[query_emb], n_results=top_k
                )
                # Return documents as list of strings
                return results["documents"][0]

            def format_docs(docs):
                return "\n\n".join(docs)

            template = ChatPromptTemplate(
                [
                    SystemMessage(
                        content="You are a helpful AI bot named Neutron created by Arnab Singha. Given a context and question, provide an appropriate answer."
                    ),
                    HumanMessagePromptTemplate.from_template(
                        """Answer the question based on the given context.
                        Context: {context}
                        Question: {question}
                        Answer:"""
                    ),
                ]
            )

            # Build chain
            rag_chain = (
                {
                    "context": RunnablePassthrough(),
                    "question": RunnablePassthrough(),
                }  # placeholders
                | template
                | model
                | StrOutputParser()
            )

            st.session_state["started"] = True
            st.session_state["messages"].append({"role": "user", "content": msgg})
            st.chat_message("user").write(msgg)
            # Show typing indicator
            typing_placeholder = st.empty()
            typing_placeholder.markdown(typing_indicator, unsafe_allow_html=True)

            query = msgg[len("resource:") :]

            prefix = msgg[0 : msgg.index(":")].lower()
            print(msgg)
            retrieved_docs = chroma_retriever(
                query, top_k=5, coll_name=f"{prefix}_embeddings"
            )
            response = rag_chain.invoke(
                {"context": format_docs(retrieved_docs), "question": query}
            )
            print(response)
            typing_placeholder.empty()
            st.session_state["messages"].append(
                {"role": "assistant", "content": response}
            )
            st.chat_message("assistant").write(response)

        else:
            prompt = ChatPromptTemplate(
                [
                    "System: You are a helpful AI bot. Your name is Neutron. Your creator is Arnab Singha. Give these as response when asked about the yourself. Otherwise don't say these.",
                    "Reply appropriately of the question given below",
                    "Here is my question:{msg}",
                ]
            )
            chain = {"msg": RunnablePassthrough()} | prompt | model | StrOutputParser()
            print(msgg)
            # Store user message
            st.session_state["started"] = True
            st.session_state["messages"].append({"role": "user", "content": msgg})
            st.chat_message("user").write(msgg)
            # Show typing indicator
            typing_placeholder = st.empty()
            typing_placeholder.markdown(typing_indicator, unsafe_allow_html=True)

            reply = chain.invoke({"msg": msgg})
            typing_placeholder.empty()
            print(reply)
            st.session_state["messages"].append({"role": "assistant", "content": reply})
            st.chat_message("assistant").write(reply)

    st.markdown(extracss, unsafe_allow_html=True)
    st.sidebar.markdown(footer, unsafe_allow_html=True)


# start main loop
if __name__ == "__main__":
    main()
