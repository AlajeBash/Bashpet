import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import requests


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_summary(search_term):
    try:
        summary = wikipedia.summary(search_term, sentences=2)
        return summary
    except Exception as e:
        print(e)
        return "Sorry, I was not able to find information on that topic."

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
            print(f'Command: {command}')
            return command
    except Exception as e:
        print(e)
        talk("Sorry, I did not get that")
        return ''

# Weather function
def get_weather(Haspolat):
    API_key = '21f6ebe6a361661195560a9709fe2a06'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={Haspolat}&appid={API_key}"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data['weather'][0]['description']
    else:
        return "Error: Could not retrieve weather data."

def run_alexa ():
    command = take_command()
    print(command)
    if "your name" in command:
        talk('My Name is Bash E-Pet')
    elif "who are you" in command:
        talk('I am Bash E-Pet, Programm to by My Boss Bashir Sani just to give him joy')
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing song')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk('Current Time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = get_summary(person)
        talk(info)
    elif 'date' in command:
        talk ('Sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'you love me' in command:
        talk('Nah i am already taken')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'google' in command:
        query = command.replace('google', '')
        webbrowser.open(f"https://www.google.com/search?q={query}")
        talk("Searching Google for " + query)
    elif 'weather' in command:
        talk(get_weather)
    else:
        talk('Please say the Command Again.')

while True:
    run_alexa()