import streamlit as st

# Define fixed commands and responses for your chatbot
chatbot_responses = {
    "hi": "Hello! How can I assist you today?",
    "how are you": "I'm just a computer program, so I don't have feelings, but I'm here to help!",
    "what's your name": "I'm a basic Streamlit chatbot.",
    "bye": "Goodbye! Have a great day!"
}

# Function to initialize the conversation state
def init_conversation():
    return []

# Function to get the current conversation
def get_conversation():
    if "conversation" not in st.session_state:
        st.session_state.conversation = init_conversation()
    return st.session_state.conversation

# Streamlit app header
st.title("Simple Chatbot")

# Instructions
st.sidebar.markdown("## Instructions")
st.sidebar.write("1. Type your message in the text input box.")
st.sidebar.write("2. Click the 'Send' button to chat with the bot.")
st.sidebar.write("3. Type 'exit' to end the conversation.")

# Initialize conversation
conversation = get_conversation()

# User input
user_input = st.text_input("You:")

# Submit button
if st.button("Send"):
    user_input = user_input.lower()
    conversation.append(f"You: {user_input}")

    if user_input in chatbot_responses:
        response = chatbot_responses[user_input]
        conversation.append(f"Bot: {response}")
    else:
        conversation.append("Bot: I'm sorry, I don't understand that.")

# Display conversation history
st.text_area("Conversation History", value="\n".join(conversation), key="conversation_history")
