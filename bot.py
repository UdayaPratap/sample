# Define fixed commands and responses for your chatbot
chatbot_responses = {
    "hi": "Hello! How can I assist you today?",
    "how are you": "I'm just a computer program, so I don't have feelings, but I'm here to help!",
    "what's your name": "I'm a basic Streamlit chatbot.",
    "bye": "Goodbye! Have a great day!"
}

# Streamlit app header
st.title("Simple Chatbot")

# Initialize conversation history
conversation = []

# Instructions
st.sidebar.markdown("## Instructions")
st.sidebar.write("1. Type your message in the text input box.")
st.sidebar.write("2. Click the 'Send' button to chat with the bot.")
st.sidebar.write("3. Type 'exit' to end the conversation.")

# User input
user_input = st.text_input("You:", "")

# Bot response and conversation loop
if st.button("Send"):
    while user_input.lower() != "exit":
        user_input = user_input.lower()
        conversation.append(f"You: {user_input}")

        if user_input in chatbot_responses:
            response = chatbot_responses[user_input]
            conversation.append(f"Bot: {response}")
            st.text(response)
        else:
            conversation.append("Bot: I'm sorry, I don't understand that.")
            st.text("Bot: I'm sorry, I don't understand that.")

        user_input = st.text_input("You:", "")

# Display conversation history
st.text_area("Conversation History", value="\n".join(conversation))
