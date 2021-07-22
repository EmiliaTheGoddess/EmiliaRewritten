import speech_recognition as sr

# Function to return spoken text
import main


def get_audio():
    # create speech recognition object
    rObject = sr.Recognizer()
    audio = ''
    # listen the microphone
    with sr.Microphone() as source:
        print("AutoListener is listening...")
        # Start listening
        audio = rObject.listen(source, phrase_time_limit=5)
    print("AutoListener stopped.")
    try:
        # Try to understand what has said with the given language
        text = rObject.recognize_google(audio, language='en-US')
        print("You: " + text)
        return text
    except:
        return 0

def startlistening():
    while True:
        try:
            text = get_audio().lower()
            # Speech recognition sometimes can't understand me
            if 'emilia' in text or 'amelia' in text or 'camellia' in text:
                break
        except:
            print("Nothing to be understood here.")
    main.startlistening()


if __name__ == "__main__":
    startlistening()