import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text to speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

engine.setProperty('voice', 'english+f1')
engine.setProperty('rate', 150)  # Speed of speech

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: ", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I did not get that")
        return listen()
    except sr.RequestError:
        print("Sorry, my speech service is down")
        return None

def speak(text):
    engine.say(text)
    engine.runAndWait()


def set_reminder(text):
    # For simplicity, just repeat what was said as a reminder.
    speak(f"Reminder is set for: {text}")



todo_list = []

def add_to_todo_list(item):
    todo_list.append(item)
    speak(f"Added {item} to your to-do list.")

def show_todo_list():
    if not todo_list:
        speak("Your to-do list is empty.")
    else:
        speak("Items on your to-do list:")
        for item in todo_list:
            speak(item)


import wikipedia

def search_web(query):
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia, " + results)


def main():
    speak("Hello, I am your assistant. How can I help you today?")
    while True:
        text = listen().lower()
        if "reminder" in text:
            set_reminder(text)
        elif "add to to-do list" in text:
            add_to_todo_list(text.replace("add to to-do list", ""))
        elif "show to-do list" in text:
            show_todo_list()
        elif "search for" in text or "search" in text:
            search_web(text.replace("search for", "").strip())
        elif "stop" in text or "exit" in text:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
