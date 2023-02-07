import SpeechRecognition as sr
import pyttsx3
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("user said : ", query)
    except Exception as e:
        print(e)
        speak("Sorry guys, can you repeat that again?")
        return "None"
    return query


if __name__ == "__main__":
    while True:
        speak("How can i help you?")
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching in wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        else:
            speak("Im not understand")
