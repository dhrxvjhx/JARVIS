'''
Modules to install:
    pip install pyttsx3 
    pip install SpeechRecognition

    pip install datetime
    pip install wikipedia
    pip install os      #If you want to open files or apps for your desktop

    If pyaudio is not showing any efforts even after instaliing so many times try pipwin
    (pip install pipwin)
    pip intsall pyaudio
'''
#Importing modules
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser   #Standard Library(No need to install)
#import os

#importing pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak ('Good Morning!')

    elif hour>=12 and hour<18:
        speak ('Good Afternoon')
    
    else:
        speak ('Good Evening')
    
    speak('Jarvis here, How may i help you?')

def takeCommand():
    #Microphone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("You said: ", query)

    except Exception as e:
        print(e)

        speak("Come again")
        print("Say that again please")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia..')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            print(results)
            speak("According to wikipedia:")
            speak(results)
        
        #websites
        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open netflix' in query:
            webbrowser.open("https://netflix.com")

        elif 'open prime' in query:
            webbrowser.open("https://primevideo.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com/")

        elif 'open github' in query:
            webbrowser.open('https://github.com/')
        
        #commands
        elif 'who are you' in query:
            print('Just','A','Rather','Very','Intelligent','System', sep='\n')
            speak('I am Just a rather very intelligent system but people like to call me Jarvis')

        elif 'hello' in query:
            speak('hello there, how are you??. how may i help you?')

        elif 'what can you do' in query:
            speak('i can do anything dhrooov sir programmed me for')

        elif "i don't know" in query:
            speak("Would you like to listen to some music, watch your favourite show or have a good sleep")

        elif 'can you help me' in query:
            speak('yes, of course')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(strTime)
        
        elif 'exit' in query:
            print('See you soon')
            speak("goodbye, ttyl")
            exit()