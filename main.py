import speech_recognition as sr
from load import *
import sys

# Define the keywords and corresponding functions
keywords = {
    "hello": lambda: print("Hello there!"),
    "chat": lambda: getFunc("chat"),
    "exit": lambda: sys.exit()
}

# Initialize the recognizer
recognizer = sr.Recognizer()

def listen_for_speech():
    with sr.Microphone() as source:
        print("Listening for speech...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Recognized speech: {text}")
            for keyword in keywords:
                if keyword in text.lower():
                    print(f"Keyword detected: {keyword}")
                    keywords[keyword]()  # Trigger the corresponding function
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        
    

if __name__ == "__main__":
    while(True):
        text = listen_for_speech()
        