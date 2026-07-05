import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

st.set_page_config(page_title="Groq Chatbot")

st.markdown("""
<style>
.user-msg {
    background-color: #DCF8C6;
    color: black;
    padding: 12px 16px;
    border-radius: 15px;
    margin: 8px 0;
    max-width: 70%;
    margin-left: auto;
    text-align: right;
}
.bot-msg {
    background-color: #F1F0F0;
    color: black;
    padding: 12px 16px;
    border-radius: 15px;
    margin: 8px 0;
    max-width: 70%;
    margin-right: auto;
    text-align: left;
}
</style>
""", unsafe_allow_html=True)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
)

MAX_QUESTIONS = 5

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]

if "question_count" not in st.session_state:
    st.session_state.question_count = 0

st.title("🤖 Groq Chatbot")
st.caption("Free session limit: 5 questions")

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f"<div class='user-msg'>{msg['content']}</div>",
            unsafe_allow_html=True
        )
    elif msg["role"] == "assistant":
        st.markdown(
            f"<div class='bot-msg'>{msg['content']}</div>",
            unsafe_allow_html=True
        )

if st.session_state.question_count >= MAX_QUESTIONS:
    st.warning("You have exhausted your free limit of 5 questions for this session.")
else:
    prompt = st.chat_input("Ask something...")

    if prompt:
        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )

        st.session_state.question_count += 1

        st.markdown(
            f"<div class='user-msg'>{prompt}</div>",
            unsafe_allow_html=True
        )

        with st.spinner("Bot is thinking..."):
            response = llm.invoke(st.session_state.messages)

        st.session_state.messages.append(
            {"role": "assistant", "content": response.content}
        )

        st.markdown(
            f"<div class='bot-msg'>{response.content}</div>",
            unsafe_allow_html=True
        )