# This code is for v1 of the openai package: pypi.org/project/openai
from openai import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key = api_key)

def chat_completion(user_input):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "system",
        "content": "You are a helpful assistant"
        },
        {
        "role": "user",
        "content": user_input
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response




# Streamlit UI
st.title("AI Chatbot")

# Input box for user input
user_input = st.text_input("You:", "")

if user_input:
    st.text("Assistant:")
    # Generate and display the chatbot response
    with st.spinner("Thinking..."):
        response = chat_completion(user_input)
        response.choices[0].message.content
        # st.success(response)

st.sidebar.text("This app uses OpenAI's GPT-3.5 turbo model.")
