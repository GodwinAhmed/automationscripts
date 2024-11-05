import random
import time  # Import time module for adding delays

def chatbot():
    """Enhanced simple chatbot function that interacts with the user."""
    responses = [
        'Hello!',
        'How can I help you?',
        'Goodbye!',
        'What are you doing today?',
        'Tell me more about yourself.',
        'I am just a simple chatbot.',
        'How can I assist you further?'
    ]
    
    while True:  # Infinite loop for continuous interaction
        user_input = input("You: ")  # Get user input
        if user_input.lower() in ['bye', 'exit', 'quit']:  # Check for multiple exit commands
            print("Chatbot: Goodbye!")  # Farewell message
            break  # Exit the loop
        
        # Simulate thinking time
        time.sleep(1)  # Wait for 1 second before responding
        print(f"Chatbot: {random.choice(responses)}")  # Respond with a random choice from responses

# Start the chatbot
chatbot()