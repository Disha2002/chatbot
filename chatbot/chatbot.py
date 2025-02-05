import openai
import random

# Set up your OpenAI API key
# openai.api_key = "you_scret_key"

def chat_with_ai():
    print("Welcome to the AI Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Goodbye!")
            break

        try:
            # Create a completion request with the latest API
            response = openai.Completion.create(
                model="gpt-3.5-turbo",  # You can use a different model if needed
                prompt=user_input,
                max_tokens=150
            )

            # Print the response from the AI
            print("AI Chatbot:", response['choices'][0]['text'].strip())

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chat_with_ai()