import pyttsx3  # Import the pyttsx3 library for text-to-speech functionality

def text_to_speech(text, voice_id=None, rate=150):
    """Convert text to speech with optional voice and rate settings."""
    try:
        engine = pyttsx3.init()  # Initialize the text-to-speech engine
        
        # Set voice if voice_id is provided
        if voice_id is not None:
            engine.setProperty('voice', voice_id)
        
        # Set the speech rate
        engine.setProperty('rate', rate)
        
        engine.say(text)  # Queue the text to be spoken
        engine.runAndWait()  # Wait for the speech to finish
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Get available voices
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    # Print available voices
    for index, voice in enumerate(voices):
        print(f"Voice {index}: {voice.name} - {voice.languages}")

    # Example: Use the first voice and set a custom rate
    text_to_speech('Hello World, Python is amazing!', voice_id=voices[0].id, rate=150)