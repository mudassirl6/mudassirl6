import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Set Hugging Face token
os.environ['HF_TOKEN'] = os.getenv("HF_TOKEN")

# Initialize embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Set up Streamlit UI
st.title("HealthCare Assistant ChatBot")
st.write("Type what you want?")

# Input the Groq API Key
api_key = os.getenv("GROQ_API_KEY")

# Initialize LLM
llm = ChatGroq(groq_api_key=api_key, model_name="Gemma2-9b-It")

# Define chat prompt template
chat_prompt = ChatPromptTemplate.from_template(
    """
    You are an AI Healthcare Assistant. Your role is to provide users with helpful health tips, 
    suggest medicines for common illnesses, and offer general wellness advice. 
    Please respond with accurate, reliable, and responsible health recommendations.
    
    User Query: {user_input}
    """
)

# User input
user_input = st.text_input("Ask me anything about healthcare:")

if st.button("Get Response") and user_input:
    prompt = chat_prompt.format(user_input=user_input)
    response = llm.invoke(prompt)
    st.write("### Health Tips & Medicines")
    st.write(response.content)