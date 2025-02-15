# You will need to enter your respective API keys

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


LANGCHAIN_API_KEY = ""
GOOGLE_API_KEY = ""


os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY



## PROMPT TEMPLATE
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
    
)

## streamlit function

st.title("Langchain Demo with LLama2")
input_text= st.text_input("Enter your question", key="input_text")

## Gemini LLM

llm= ChatGoogleGenerativeAI(model= "gemini-1.5-pro")
output_parser= StrOutputParser()
chain= prompt | llm | output_parser
