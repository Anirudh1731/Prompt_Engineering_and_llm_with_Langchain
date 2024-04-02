import streamlit as st
import langchain
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import openai
# need llm chain whener dealing with prompts
from langchain.chains import LLMChain
import os

os.environ["OPENAI_API_KEY"]=""
template1='''I want you to act as a financial advisor for people. In an easy way , explain basics of {financial_concept}'''


prompt=PromptTemplate(
    input_variables=['financial_concept'],
    template=template1
)


llm=openai.OpenAI(temperature=0.8)
chain1=LLMChain(llm=llm,prompt=prompt)
st.title("Financial advisor nandu ")
input_text=st.text_input("Search the topic")

if input_text:
    st.write(chain1({'financial_concept':input_text}))