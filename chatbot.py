import streamlit as st
from huggingface_hub import InferenceClient

client = InferenceClient()

st.title("Vandana's AI Chatbot")

message = st.chat_input("Type your message...")

if message:
    st.chat_message("user").write(message)

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "user", "content": message}
        ],
        max_tokens=200
    )

    st.chat_message("assistant").write(
        response.choices[0].message.content
    )
    