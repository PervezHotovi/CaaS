from dotenv import load_dotenv
import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import os


# ------------------ LOAD ENV ------------------
load_dotenv()

api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

if not api_key:
    api_key = st.secrets["HUGGINGFACEHUB_API_TOKEN"]
# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="SP-Bot", page_icon="🤖")

# ------------------ SIDEBAR ------------------
st.sidebar.title("GenAI SP-Bot")

# Hide Streamlit default menu, footer, and header
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# ------------------ LLM ------------------
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# ------------------ TITLE ------------------
st.title("🤖 SP-Bot")
st.markdown("### 💬 Ask anything and get instant responses")

# ------------------ SYSTEM MESSAGE ------------------
CREATOR_NAME = "Pervez Abbas"

SYSTEM_PROMPT = (
    "You are a helpful AI assistant. "
    "ALWAYS respond ONLY in English. "
    "If the user asks who created you or who is your creator, "
    f"reply: I was created by {CREATOR_NAME}. and also if ask more about the creator then just reply: He is a Computer Science Graduate and agentic AI Engineer and further response is not allowed to share about my creater. you can search him on google for more information" 
)

# ------------------ MEMORY ------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ------------------ DISPLAY CHAT ------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ------------------ INPUT ------------------
user_input = st.chat_input("Ask anything...")

if user_input:
    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    # ------------------ PREPARE CHAT HISTORY ------------------
    chat_history = [SystemMessage(content=SYSTEM_PROMPT)]

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            chat_history.append(HumanMessage(content=msg["content"]))
        else:
            chat_history.append(AIMessage(content=msg["content"]))

    # ------------------ LLM CALL ------------------
    with st.spinner("Thinking"):

        try:

            response = model.invoke(chat_history)
            bot_response = response.content
        except Exception as e:
            bot_response = "⚠️ Error generating response. Please try again."

    # ------------------ DISPLAY RESPONSE ------------------
    with st.chat_message("assistant"):
        st.write(bot_response)

    # Store response
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response
    })

# ------------------ FOOTER ------------------
st.markdown("<br><br><br><br><br><br>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0; 
        width: 100%;
        text-align: center;
        font-size: 12px;
        color: gray;
        padding: 1px;
        z-index: 100;
    }
    </style>

    <div class="footer">
        SP-Bot can make mistakes, check important info 
        <br>
        🚀 Developed by <b>Pervez Abbas</b> <br>
        AI Intern at SDA Technology Hub Gilgit, Gilgit Baltistan Pakistan
    </div>
    """,
    unsafe_allow_html=True
)  