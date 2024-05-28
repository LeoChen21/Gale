import speech_recognition as sr
from load import *

def recognize_speech_from_mic():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default system microphone as the audio source
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")
        # Listen for 5 seconds and create ambient noise energy level
        recognizer.adjust_for_ambient_noise(source, duration=5)
        print("Microphone calibrated. Listening...")

        # Listen for the first phrase and extract it into audio data
        audio = recognizer.listen(source)
        print("done")

    # Recognize (convert from speech to text)
    try:
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        
    

if __name__ == "__main__":
    text = recognize_speech_from_mic()
    if(text):
        getFunc(text)