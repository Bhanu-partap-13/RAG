from langchain_huggingface import HuggingFacePipeline, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

# why we need prompt template?
# We have to kind of prompts one of them is static and other is dynamic.
# # Static prompt is the one which is fixed and we can use it for multiple inputs.
#  Dynamic prompt is the one which is changing based on the input. 
# So we need to create a prompt template which will help us to create dynamic prompts. 
# Yess, but we use F" strings too> why not that is the very goood question.
# There are three core features that f"string do not have.
# 1. Reusable: We can mantain this prompt in seperate file(like json) and can use it by calling a function.
# 2. validation: Think that in the dynamic prompt you have not provided the input for the variable, If you have written validateTrue It will autmotically fetch whether you have 
# written the inputs or not, If not it will take all the valid in the template
#  
load_dotenv()

st.header("Risk Assessment")

user_input = st.text_input("Enter your prompt for theassesment")

if st.button("Summarize"):
    result = model.invoke(user_input)
    st.text("Processing your request...") 