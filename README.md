# Bash E-Pet (Version 1.0) 
## Introduction
Bash E-Pet is a voice-activated virtual assistant created using Python. It utilizes various libraries to perform tasks such as speech recognition, text-to-speech conversion, web scraping, and more.

## Features
1. **Voice Interaction:** Bash E-Pet listens for voice commands and responds accordingly.
2. **Basic Information Retrieval:** It can fetch summaries from Wikipedia about specific topics.
3. **Entertainment:** Bash E-Pet can play songs on YouTube, tell jokes, and search the web.
4. **Time and Weather:** It provides the current time and weather information for a specified location.
5. **Personal Responses:** It has predefined responses to certain personal questions and inquiries.

## Dependencies
- `speech_recognition:` For recognizing speech input from the user.
- `pyttsx3:` For converting text to speech for responses.
- `pywhatkit:` For accessing YouTube to play songs.
- `datetime:` For retrieving current date and time.
- `wikipedia:` For fetching summaries from Wikipedia.
- `pyjokes:` For generating random jokes.
- `webbrowser:` For opening web browser for Google searches.
- `requests:` For making HTTP requests to fetch weather data.

## Functions
1. talk(text)<br>
   Parameters: text (str) - The text to be spoken.<br>
   Description: Converts the given text into speech and speaks it aloud.<br>

2. get_summary(search_term)<br>
   Parameters: search_term (str) - The topic to search on Wikipedia.<br>
   Returns: A summary of the topic from Wikipedia, or an error message if not found.<br>
   Description: Fetches a summary of the specified topic from Wikipedia.<br>

3. take_command()<br>
   Description: Listens for voice input from the user, recognizes it, and returns the command.

4. get_weather(location)<br>
   Parameters: location (str) - The location for which weather information is needed.<br>
   Returns: A description of the weather or an error message if data cannot be retrieved.<br>
   Description: Retrieves the current weather information for the specified location using OpenWeatherMap API.<br>

5. run_alexa()<br>
   Description: Executes the main functionality of Bash E-Pet based on user commands. It recognizes various commands such as asking for the assistant's name, playing music, fetching time, retrieving information about a person, telling jokes, searching Google, checking the weather, and responding to personal questions.

## Usage
1. Import the required libraries.
2. Initialize the speech recognition and text-to-speech engines.
3. Define functions for handling various tasks.
4. Call the run_alexa() function in a loop to continuously listen for and respond to user commands.

## Example
```python
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import requests

# Define functions and main loop

while True:
    run_alexa()
```

## Notes
- Ensure an active internet connection for fetching data from Wikipedia and weather information.
- Some functionalities may require API keys or permissions, such as the OpenWeatherMap API for weather data.

NOTE:** This project is under development, so some features may not work or work accurately.

## Author
BASHIR SANI <br>
[LinkedIn](www.linkedin.com/in/alajeebash)<br>
[Github](https://github.com/AlajeBash)
