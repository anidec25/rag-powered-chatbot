from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


# Initialize the language model
llm = ChatOpenAI(model="gpt-4o-mini")

# Initialize Streamlit app
st.title("Chatbot - 1 Hour Project")

# Sidebar for additional settings or information
st.sidebar.title("Settings")
st.sidebar.markdown("Adjust your preferences here.")

# Text input for user's name in the sidebar
user_name = st.sidebar.text_input("Enter your name", "User")

# Color pickers for user and assistant message backgrounds
user_color = st.sidebar.color_picker("Pick a color for user messages", "#5DA02D")
assistant_color = st.sidebar.color_picker("Pick a color for assistant messages", "#100D0D")

# Custom CSS for styling
st.markdown(
    f"""
    <style>
    .user-message {{ background-color: {user_color}; padding: 10px; border-radius: 5px; color: white; }}
    .assistant-message {{ background-color: {assistant_color}; padding: 10px; border-radius: 5px; color: white; }}
    .message-container {{ margin-bottom: 10px; }}
    .stButton > button {{ background-color: #ff4b4b; color: white; width: 150px; }}
    .sidebar .stButton > button {{ width: 100%; white-space: nowrap; }}
    </style>
    """,
    unsafe_allow_html=True
)

# Clear conversation history button in the sidebar
if st.sidebar.button("Clear Conversation"):
    st.session_state.conversation = []

# Initialize session state for conversation history
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Function to handle user input and get response
def get_response(user_input):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant. Please respond to the user queries."),
            ("user", f"Question: {user_input}")
        ]
    )
    response = llm.invoke(user_input)
    return response.content

# User input
user_input = st.text_input("Type your message here...")

# Adjust column widths to move the Send button slightly to the left
col1, col2, col3 = st.columns([1.5, 1, 1.5])

with col2:
    if st.button("Send"):
        if user_input:
            # Append user input to conversation
            st.session_state.conversation.append((user_name, user_input))
            
            # Get response from the model
            response = get_response(user_input)
            
            # Append model response to conversation
            st.session_state.conversation.append(("Jarvis", response))

# Display the conversation history in reverse order
for i in range(len(st.session_state.conversation) - 2, -1, -2):
    user_message = st.session_state.conversation[i]
    assistant_message = st.session_state.conversation[i + 1] if i + 1 < len(st.session_state.conversation) else None
    
    # Display user message
    st.markdown(f'<div class="message-container"><div class="user-message"><strong>{user_message[0]}:</strong> {user_message[1]}</div></div>', unsafe_allow_html=True)
    
    # Display assistant message if it exists
    if assistant_message:
        st.markdown(f'<div class="message-container"><div class="assistant-message"><strong>{assistant_message[0]}:</strong> {assistant_message[1]}</div></div>', unsafe_allow_html=True)
