import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

API_KEY = "AIzaSyBolyLRVMitWnRWCVnigpV4WNGsOeHCuCw"

st.title("Neutron")

model=ChatGoogleGenerativeAI(google_api_key=API_KEY,model="gemini-1.5-pro")
st.markdown('''#### Hi! Let's get started.''')

msgg=st.text_input("Type in your message for me")

prompt=ChatPromptTemplate(["Here is my message:{msg}"])
chain=({"msg":RunnablePassthrough()}|prompt|model|StrOutputParser())
reply=chain.invoke(msgg)

st.write(reply)
st.text("Developed by: Arnab Singha")
