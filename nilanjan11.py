import os
import time
import requests
import speech_recognition as sr
import pywhatkit as kit
import wikipedia
import pyjokes
import pyautogui
import pyttsx3
from datetime import datetime
from decouple import config
from utils import opening_text
from os_ops import open_camera, open_notepad, open_discord, open_cmd, open_calculator
from functions.online_ops import find_my_ip

def greet_user():
    current_hour = int(datetime.now().hour)
    if 21 <= current_hour or current_hour < 6:
        return "Good Night"
    elif 6 <= current_hour < 12:
        return "Good Morning"
    elif 12 <= current_hour < 18:
        return "Good Afternoon"
    else:
        return "Good Evening"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_google():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Error: ", e)
        speak("Sorry, I didn't get that. Please try again.")
        return None
    return query

def jarvis():
    while True:
        query = recognize_google()
        if query is None:
            continue
        elif "exit" in query or "stop" in query:
            speak("Goodbye!")
            break
        elif "hello" in query or "hi" in query:
            speak(f"{greet_user()}, I am your assistant JARVIS. How can I help you?")
        elif "notepad" in query:
            open_notepad()
            speak("Opening Notepad++")
        elif "discord" in query:
            open_discord()
            speak("Opening Discord")
        elif "camera" in query:
            open_camera()
            speak("Opening Camera")
        elif "calculator" in query:
            open_calculator()
            speak("Opening Calculator")
        elif "ip" in query:
            ip = find_my_ip()
            speak(f"Your IP address is {ip}")
        elif "wikipedia" in query:
            try:
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                speak(result)
            except Exception as e:
                print("Error: ", e)
                speak("Sorry, I couldn't find anything on Wikipedia.")
        elif "joke" in query:
            speak(pyjokes.get_joke())
        elif "open" in query:
            os.startfile(query.replace("open", ""))
            speak("Opening the requested software")
        elif "time" in query:
            current_time = datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")
        elif "date" in query:
            current_date = datetime.now().strftime("%d %B %Y")
            speak(f"The current date is {current_date}")
        elif "weather" in query:
            try:
                api_key = config("WEATHER_API_KEY")
                base_url = "http://api.openweathermap.org/data/2.5/weather?"
                city_name = query.replace("weather", "")
                complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                response = requests.get(complete_url)
                data = response.json()
                weather = data["weather"][0]["description"]
                speak(f"The weather in {city_name} is {weather}")
            except Exception as e:
                print("Error: ",)
