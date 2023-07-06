import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random
import requests
import json
import time
import subprocess as sp

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for voice commands
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User: {query}\n")
    except Exception as e:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return ""

    return query

# Function to perform actions based on voice commands
def process_command(command):
    command = command.lower()

    if "greet" in command:
        greetings = ["Hello!", "Hi there!", "Greetings!"]
        speak(random.choice(greetings))

    elif "wikipedia" in command:
        speak("Searching Wikipedia...")
        query = command.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=12)
        speak("According to Wikipedia:")
        print(results)
        speak(results)

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
    elif 'play music' in command:
        webbrowser.open("spotify.com")

    elif 'open instagram' in command:
        webbrowser.open("instagram.com")
    elif 'the time' in command:
        strTime = datetime.datetime.now().strftime("%H:%M :%S")
        speak(f"the time is {strTime}")
    elif 'open maps ' in command:
        webbrowser.open("https://www.google.com/maps/@17.6001492,78.4410784,15z?entry=ttu")
    elif 'gpt' in command:
        webbrowser.open('https://chat.openai.com/')

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")


    elif "open camera" in command:
        sp.run('start microsoft.windows.camera:', shell=True)





    elif "open system preferences" in command:
        os.system(
            "open /System/Library/PreferencePanes/Security.prefPane")  # Replace with the command for opening the specific system preference on your macOS system

    elif 'play music' in command:
        webbrowser.open("spotify.com")
    elif 'open google' in command:
        webbrowser.open("google.com")
    elif 'open instagram' in command:
        webbrowser.open("instagram.com")


    elif ' maps ' in command:
        webbrowser.open("https://www.google.com/maps/@17.6001492,78.4410784,15z?entry=ttu")
    elif 'open chat gpt' in command:
        webbrowser.open('https://chat.openai.com/')
    elif " song" in command:
        music_dir = r"C:\Users\saipr\Downloads\pata"
        music_files = os.listdir(music_dir)
        if music_files:
            random.shuffle(music_files)
            os.startfile(os.path.join(music_dir, music_files[0]))
        else:
            speak("No music files found in the specified folder.")

    elif "how are you" in command:
        responses = ["I'm good, thank you!", "I'm fine, thanks for asking.", "I'm doing great!"]
        speak(random.choice(responses))

    elif "joke" in command:
        jokes = ["Why don't scientists trust atoms? Because they make up everything!",
                 "Did you hear about the mathematician who's afraid of negative numbers? He will stop at nothing to avoid them!",
                 "Why don't skeletons fight each other? They don't have the guts!",
                 "I told my wife she should embrace her mistakes. She hugged me.",

                 "I asked the librarian if she had any books on paranoia. She whispered, 'They're right behind you.'",

                 "Why don't scientists trust atoms? Because they make up everything... but they never share!",

                 "I used to play piano by ear, but now I use my hands.",

                 "Why don't skeletons fight each other? They don't have the guts... or the muscles... or the tendons."
                 ]
        speak(random.choice(jokes))

    elif "news" in command:
        speak("Here are the latest news headlines:")
        webbrowser.open("https://timesofindia.indiatimes.com/")



    elif "weather" in command:
        speak("Sure, please provide the name of the city.")
        city = listen()
        webbrowser.open("https://www.accuweather.com/en/in/hyderabad/202190/weather-forecast/202190")


    elif "reminder" in command:
        speak("Sure, please provide the reminder message.")
        reminder_message = listen()
        if reminder_message:
            speak("Please provide the number of seconds after which you want to be reminded.")
            reminder_delay = int(listen())
            if reminder_delay:
                try:
                    reminder_delay = int(reminder_delay)
                    if reminder_delay >= 0:
                        speak("Setting the reminder. I will notify you after the specified time.")
                        time.sleep(reminder_delay)
                        speak(f"Reminder: {reminder_message}")
                    else:
                        speak("Sorry, the reminder delay should be a non-negative number.")
                except ValueError:
                    speak("Sorry, the reminder delay should be a valid number of seconds.")
            else:
                speak("Sorry, I didn't catch the reminder delay. Please try again.")
        else:
            speak("Sorry, I didn't catch the reminder message. Please try again.")
    elif "motivation" in command:
        quotes = ["The only way to do great work is to love what you do. - Steve Jobs",
                  "Innovation distinguishes between a leader and a follower. - Steve Jobs",
                  "Your time is limited, don't waste it living someone else's life. - Steve Jobs"
                  "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",

                  "Believe you can and you're halfway there. - Theodore Roosevelt",



                  "The only way to do great work is to love what you do. - Steve Jobs",


                  "The harder you work for something, the greater you'll feel when you achieve it. - Unknown",

                  "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D.Roosevelt " ,



                  "The best way to predict the future is to create it.- Peter Drucker",


                  ]
        speak(random.choice(quotes))

    elif "end it" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I didn't understand that.")

# Greet the user
speak("Hello! I'm desktop assistant. How can I assist you today?")

# Main program loop
while True:
    command = listen()
    process_command(command)

