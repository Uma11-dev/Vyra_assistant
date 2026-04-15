import streamlit as st
import requests

st.set_page_config(page_title="Vyra", page_icon="🌙")

st.title("Vyra — Luna’s Sanctum 🤍")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Input
user_input = st.chat_input("Ask your question...")

if user_input:
    # Show user message
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Call your API
    response = requests.post(
        "http://127.0.0.1:8000/chat",
        params={"query": user_input}
    )

    reply = response.json()["response"]

    # Show bot response
    st.chat_message("assistant").write(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})