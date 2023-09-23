import streamlit as st

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

widget_counter = 1

# User input
user_input = st.text_input("You:", key=f"chat_input_{widget_counter}")
widget_counter += 1

# Create a form for the chat interaction
with st.form("chat_form"):
    # Submit button
    submit_button = st.form_submit_button("Send", key=f"submit_button_{widget_counter}")

# Bot response and conversation loop
while user_input.lower() != "exit":
    if submit_button:
        user_input = user_input.lower()
        conversation.append(f"You: {user_input}")

        if user_input in chatbot_responses:
            response = chatbot_responses[user_input]
            conversation.append(f"Bot: {response}")
            st.write(f"Bot: {response}", key=f"response_{widget_counter}")
        else:
            conversation.append("Bot: I'm sorry, I don't understand that.")
            st.write("Bot: I'm sorry, I don't understand that.", key=f"response_{widget_counter}")

        # Create a new form for the next interaction
        with st.form("chat_form"):
            user_input = st.text_input("You:", key=f"chat_input_{widget_counter}")
            submit_button = st.form_submit_button("Send", key=f"submit_button_{widget_counter}")

        widget_counter += 1

# Display conversation history
st.text_area("Conversation History", value="\n".join(conversation), key="conversation_history")
