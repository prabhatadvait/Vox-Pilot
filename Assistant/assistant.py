import speech_recognition as sr
import datetime
import webbrowser
import pyttsx3
import pywhatkit

engine = pyttsx3.init()
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print("Clearing background noises...Please wait")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print('Ask me anything..')
        recordedaudio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(recordedaudio, language='en_US')
        text = text.lower()
        print('Your message:', text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return

    if 'chrome' in text:
        a = 'Opening Chrome..'
        engine.say(a)
        engine.runAndWait()
        webbrowser.open('http://www.google.com')  # Replace with the desired URL

    elif 'time' in text:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()

    elif 'play' in text:
        a = 'Opening YouTube..'
        engine.say(a)
        engine.runAndWait()
        pywhatkit.playonyt(text)

    elif 'youtube' in text:
        b = 'Opening YouTube'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('http://www.youtube.com')

    elif 'stop' in text:
        engine.say('Stopping the program.')
        engine.runAndWait()
        exit()

while True:
    cmd()
