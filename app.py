import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

api_key = st.secrets["API_KEY"]
st.set_page_config(page_title="Neutron☄️⭐🌟🌍👽🤖☄",page_icon="🤖")
st.markdown("<h1 class=hdr>Neutron</h1>",True)

model=ChatGoogleGenerativeAI(google_api_key=api_key,model="gemini-1.0-pro")
st.markdown('''#### Hey there! Let's start.''')

msgg=st.text_input("Type in your message for me")

if len(msgg)>0:
	prompt=ChatPromptTemplate([("System: Always remember :- You are a helpful AI bot. Your name is Neutron. Your creator is Arnab Singha. Arnab Singha is a student of Computer Science. He is from Midnapore, West Bengal, India. Give these as response when asked about the respectives. Carefully remember that you are not gemini and Google is not your creator. Please don't ever say that you are gemini and Google made you. But please don't say these if not asked about"),
				   ("Here is my message:{msg}")])
	chain=({"msg":RunnablePassthrough()}|prompt|model|StrOutputParser())
	reply=chain.invoke(msgg)
	st.write(reply)

footer = """
    <style>
        .hdr{
            text-shadow: 0px 0px 15px red;
            animation: colranim 15s ease infinite;
        }
        @keyframes colranim {
        0%{
            text-shadow: 0px 0px 15px red;
        }
        10%{
            text-shadow: 0px 0px 15px cyan;
        }
        20%{
            text-shadow: 0px 0px 15px green;
        }
        30%{
            text-shadow: 0px 0px 15px blue;
        }
        40%{
            text-shadow: 0px 0px 15px yellow;
        }
        50%{
            text-shadow: 0px 0px 15px magenta;
        }
        60%{
            text-shadow: 0px 0px 15px hotpink;
        }
        70%{
            text-shadow: 0px 0px 15px orange;
        }
        80%{
            text-shadow: 0px 0px 15px smokewhite;
        }
        90%{
            text-shadow: 0px 0px 15px purple;
        }
        100%{
            text-shadow: 0px 0px 15px red;
        }
    }
        /* Hide Streamlit's main menu (hamburger menu) */
        header {visibility: hidden;}

        /* Hide Streamlit's footer */
        footer {visibility: hidden;}

        /* Hide the watermark ("Made with Streamlit") */
        .st-emotion-cache-z5fcl4 {display: none;}
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: rgb(20,20,20);
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 14px;
            box-shadow: 0 -4px 5px rgba(200,100,100, 0.1);
        }
    </style>
    <div class="footer">
        👨‍💻 Developed by <a style="text-decoration:none;color:red" href="https://arnabsingha200228.github.io/my-portfolio/" target="_blank">Arnab Singha</a> | 
        📧 <a style="text-decoration:none;color:red" href="mailto:arnabsingha200228@gmail.com">Contact Us</a>
    </div>
"""
st.markdown(footer,True)
