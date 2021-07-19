"""
Emilia the helpful assistant

Currently works on GNU/Linux
To make it work on w*ndows just edit the file paths

"""

import speech_recognition as sr
import os
from playsound import playsound

import autolisten
from modules.parsetext import *

# The path script is running in.
currentfilepath = os.path.dirname(os.path.realpath(__file__))


# Function to return spoken text
def get_audio():
    # create speech recognition object
    rObject = sr.Recognizer()
    audio = ''
    # listen the microphone
    with sr.Microphone() as source:
        print("Main function is listening...")
        # Start listening
        audio = rObject.listen(source, phrase_time_limit=5)
    print("Main function stopped listening.")
    try:
        # Try to understand what has said with the given language
        text = rObject.recognize_google(audio, language='en-US')
        print("You: " + text)
        return text
    except:
        return 0


def startlistening():
    playsound('/home/dsf001/PycharmProjects/EmiliaRewritten/sounds/start.mp3')
    spokentext = get_audio().lower()
    check(spokentext)
    autolisten.startlistening()

if __name__ == "__main__":
    startlistening()