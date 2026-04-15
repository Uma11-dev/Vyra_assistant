import streamlit as st
from app.rag import ask_vyra

# Page config
st.set_page_config(
    page_title="Vyra — Luna's Sanctum",
    page_icon="🌙",
    layout="centered"
)

# Header
st.title("🌙 Vyra")
st.caption("Your guide to Luna's Sanctum. Ask me anything about our sessions.")

# Initialize chat history in session
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask Vyra something..."):

    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get Vyra's response
    with st.chat_message("assistant"):
        with st.spinner("Vyra is thinking..."):
            reply, st.session_state.chat_history = ask_vyra(
                prompt,
                st.session_state.chat_history
            )
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})