import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

api_key = st.secrets["API_KEY"]
st.set_page_config(page_title="Neutron☄️⭐🌟🌍👽🤖☄",page_icon="⚛️🤖")
st.title("Neutron")

model=ChatGoogleGenerativeAI(google_api_key=api_key,model="gemini-1.0-pro")
st.markdown('''#### Hi! Let's get started.''')

msgg=st.text_input("Type in your message for me")

if len(msgg)>0:
	prompt=ChatPromptTemplate(["System: You are a helpful AI bot. Your name is Neutron. Your creator is Arnab Singha. Arnab Singha is a student of Computer Science. He is from Midnapore, West Bengal, India. Give these as response when asked about the respectives.",
				   "Here is my message:{msg}"])
	chain=({"msg":RunnablePassthrough()}|prompt|model|StrOutputParser())
	reply=chain.invoke(msgg)
	st.write(reply)

footer = """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: rgba(255,255,255,0.7);
            color: #000;
            text-align: center;
            padding: 10px;
            font-size: 14px;
            box-shadow: 0 -1px 5px rgba(0, 0, 0, 0.1);
        }
    </style>
    <div class="footer">
        👨‍💻 Developed by <a href="" target="_blank">Arnab Singha</a> | 
        📧 <a href="mailto:arnabsingha200228@gmail.com">Contact Us</a>
    </div>
"""
st.markdown(footer,True)
st.markdown('''
<script>
	document.title="Neutron"
 </script>
''',True)
