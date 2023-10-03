def user_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input or "hey" in user_input or "helo" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a computer program, but I'm here to help. What can I do for you?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "what is your name" in user_input:
        return "I'm just a chatbot. You can call me ."
    else:
        return "I'm not sure how to respond to that. Can you please rephrase your question?"

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Chatbot: Goodbye!")
        break
    response = user_response(user_input)
    print("Chatbot:", response)
