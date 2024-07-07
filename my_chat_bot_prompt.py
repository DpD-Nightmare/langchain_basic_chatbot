from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser #String O/p parser also for custom output parser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv
# import ollama
# print(dir(ollama))
load_dotenv()
#Load the keys
# Langchain monitering
os.environ['API_KEY']= 'API_KEY'


os.environ['Langsmith tresser'] = 'true'#Langsmith treser
os.environ["APIKEY"]=os.getenv("APIKEY")

#Propt templet

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a healpful assistant. please response to the user queries"),
        ("user","Question:{question}")
    ]
)

#Streamlit framework
st.title('Langchain Demo with LAMMA3 Model')
input_text = st.text_input("Search the topic u want")

#OpenAI LLM 
# llm = ChatOpenAI(model="gpt-3.5-turbo")
llm= Ollama(model="llama2")
op_parser = StrOutputParser()
chain = prompt|llm|op_parser

#When press enter it will start replaying
if input_text:
    st.write(chain.invoke({'question': input_text}))