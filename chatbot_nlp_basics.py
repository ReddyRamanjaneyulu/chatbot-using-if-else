# chatbot_nlp_basics.py

def chatbot():
    print("Chatbot: Hello! I'm your simple NLP chatbot. Type 'bye' to exit.\n")

    while True:
        # Step 1: Input (user speaks)
        user_input = input("You: ")

        # Step 2: Preprocessing (NLP Step - make it lowercase, remove extra spaces)
        user_input = user_input.strip().lower()

        # Step 3: Pattern Matching (Rule-Based Logic)
        if user_input == "hi":
            print("Chatbot: Hello!")
        elif user_input == "hello":
            print("Chatbot: Hi there!")
        elif user_input == "how are you":
            print("Chatbot: I'm a chatbot, but I'm functioning as expected!")
        elif user_input == "what is your name":
            print("Chatbot: My name is RuleBot.")
        elif user_input == "bye":
            print("Chatbot: Bye! Have a nice day.")
            break
        else:
            print("Chatbot: I'm not sure what you mean. Try saying 'hello', 'how are you', or 'bye'.")

# Run chatbot
if __name__ == "__main__":
    chatbot()
