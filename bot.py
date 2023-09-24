# import streamlit as st

# # Define fixed commands and responses for your chatbot
# chatbot_responses = {
#     "hi": "Hello! How can I assist you today?",
#     "how are you": "I'm just a computer program, so I don't have feelings, but I'm here to help!",
#     "what's your name": "I'm a basic Streamlit chatbot.",
#     "bye": "Goodbye! Have a great day!"
# }

# # Function to initialize the conversation state
# def init_conversation():
#     return []

# # Function to get the current conversation
# def get_conversation():
#     if "conversation" not in st.session_state:
#         st.session_state.conversation = init_conversation()
#     return st.session_state.conversation

# # Streamlit app header
# st.title("Simple Chatbot")

# # Instructions
# st.sidebar.markdown("## Instructions")
# st.sidebar.write("1. Type your message in the text input box.")
# st.sidebar.write("2. Click the 'Send' button to chat with the bot.")
# st.sidebar.write("3. Type 'exit' to end the conversation.")

# # Initialize conversation
# conversation = get_conversation()

# # User input
# user_input = st.text_input("You:")

# # Submit button
# if st.button("Send"):
#     user_input = user_input.lower()
#     conversation.append(f"You: {user_input}")

#     if user_input in chatbot_responses:
#         response = chatbot_responses[user_input]
#         conversation.append(f"Bot: {response}")
#     else:
#         conversation.append("Bot: I'm sorry, I don't understand that.")

# # Display conversation history
# st.text_area("Conversation History", value="\n".join(conversation), key="conversation_history")

import streamlit as st
scraped_data={
        'title': "a",
        'price': "b",
        'description': "c",
        'rating':"d",
        'reviews_count': "e",
        'availability': "f"
}
st.subheader("Chat with SHopy - Your Shopping Assistant")

 chatbot_responses = {
'title': ['name', 'title', 'brand', 'product name', 'what is it called'],
'price': ['price', 'cost', 'how much', 'value', 'worth', 'expense'],
'description': ['short description', 'brief description', 'describe', 'details', 'detail', 'specs', 'specifications', 'features'],
'rating': ['rating', 'ratings', 'rated', 'stars', 'feedback', 'reviews'],
'reviews_count': ['reviews count', 'no of reviews', 'number of reviews', 'how many reviews'],
'availability': ['deliver', 'delivery', 'available', 'availability', 'in stock', 'can I buy it'],
'all_info': ['display all data', 'display all info', 'display all information', 'give all info', 'show everything', 'show all details']
}

    # Function to initialize the conversation state
def init_conversation():
    return []
    # Function to get the current conversation
def get_conversation():
    if "conversation" not in st.session_state:
        st.session_state.conversation = init_conversation()
    return st.session_state.conversation
# Initialize conversation
conversation = get_conversation()
# User input
user_input = st.text_input("You:")
    
    # Submit button
if st.button("Send"):
    user_input = user_input.lower()
    conversation.append(f"You: {user_input}")
    found_match = False
    for key, synonyms in chatbot_responses.items():
        for synonym in synonyms:
            if synonym in user_input.lower():
                if key=='all_info':
                    response=f"Here are all the details of the product:\n{chatbot_responses}"
                    found_match=True
                else:
                    response=f"The {key} of the product is: {str(chatbot_responses[key])}"
                    found_match=True
                    
    if not found_match:
        response = "I'm sorry, I didn't understand your question. Could you please rephrase it?"
    conversation.append(response)

# Display conversation history
st.text_area("Conversation History", value="\n".join(conversation), key="conversation_history")
