## create a celebrity search application

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import os
from langchain.schema import HumanMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser







LANGCHAIN_API_KEY = "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"
GOOGLE_API_KEY = "AIzaSyAm1fVksAZ6p4OoEFGmdw5JJxpETsiP8Kc"


os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY

llm = ChatGoogleGenerativeAI(model= "gemini-1.5-pro")


st.title("Langchain Search for a celebrity")
input_text = st.text_input("Enter a celebrity name")


# prompt template

first_input_prompt =PromptTemplate(
    input_variables= ['name'],
    template = "Tell me about this {name}",
    
)



second_prompt = PromptTemplate(
    input_variables= ["name"],
    template=" When was {name} born?"
)



output_parser= StrOutputParser()
chain= first_input_prompt | llm | second_prompt | llm| output_parser
    
if input_text:
    messages = [HumanMessage(content=input_text)]
    response = llm.invoke(messages)
    st.write(response.content)
