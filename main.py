import speech_recognition as sr
from load import *
from chatgpt import *
import sys

# Define the keywords and corresponding functions
keywords = {
    "hello": lambda x: print("Hello there!"),
    "chat": lambda x: getFunc("chat"),
    "exit": lambda x: sys.exit(),
    "test": lambda x: print(x,x),
    "query": lambda x: displayResponse(x), 
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
                    response = keywords[keyword](text.lower())  # Trigger the corresponding function
                    
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

from tkinter import *

def displayResponse(x):
    response = get_chatgpt_response(x)
    # Create the main window
    window = Tk()
    window.title("Chatgpt Response:")

    # Set the window size (optional)
    window.geometry("400x200")

    # Create a label to display the text
    label = Label(window, text="Question: " + x + "\nResponse: " + response, font=("Arial", 12), wraplength=200)  # Set wraplength to desired width
    label.pack()

    # Start the event loop to keep the window open
    window.mainloop()
    

if __name__ == "__main__":
    while(True):
        text = listen_for_speech()
        
