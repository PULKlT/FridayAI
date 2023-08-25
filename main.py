import time  # Provides various time-related functions.
import webbrowser  # Allows you to open URLs in a web browser.
import speech_recognition as sr  # Provides speech recognition capabilities.
import win32com.client  # Enables communication with COM objects on Windows systems.
import subprocess  # Allows you to create and manage subprocesses (external commands).
import platform  # Provides information about the operating system and hardware.
import pygame  # A multimedia library for games and media applications.
import os  # Provides a way to interact with the operating system (e.g., file operations).
import datetime


# Function to play audio using pygame mixer.
def play_audio(file_path):
    pygame.mixer.init()  # Initialize audio playback.
    pygame.mixer.music.load(file_path)  # Load the audio file.
    pygame.mixer.music.play()  # Start playing the audio.

    while pygame.mixer.music.get_busy():  # Wait for audio to finish.
        pygame.time.Clock().tick(10)  # Control loop speed.


# Function for text-to-speech using SAPI.SpVoice
speaker = win32com.client.Dispatch("SAPI.SpVoice")


def say(text):
    speaker.Speak(text)


# Function to capture and recognize user's speech input.
def takeCommand():
    r = sr.Recognizer()  # Initialize speech recognizer.

    with sr.Microphone() as source:  # Use microphone as audio source.
        # r.pause_threshold = 0.8  # Can customize pause threshold.
        audio = r.listen(source)  # Listen for audio input.

        try:
            print("Recognising")
            user_query = r.recognize_google(audio, language="en-in")  # Recognize speech.
            print(f"User said: {user_query}")
            return user_query
        except Exception as e:
            return "Sorry, please speak again."


# Function to play audio using platform-specific commands.
def playMusic(file_path):
    if platform.system() == 'Darwin':
        subprocess.run(['afplay', file_path])  # Play audio on macOS.
    elif platform.system() == 'Windows':
        subprocess.run(['start', '/b', 'KMPlayer64', file_path], shell=True)  # Play audio on Windows.
    elif platform.system() == 'Linux':
        subprocess.run(['aplay', file_path])  # Play audio on Linux.
    else:
        print("Unsupported platform.")  # Print if platform is not recognized.


# Main script to interact with the AI assistant.
if __name__ == '__main__':
    # print("Enter what you want me to speak")
    # s = input()
    sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"],
             ["spotify", "https://spotify.com"],
             ["google", "https://google.com"], ["github", "https://github.com"], ["youtube", "https://youtube.com"],
             ["chat gpt", "https://chat.openai.com"]]
    # todo add more apps
    apps = [["intellij", "C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2022.3.2\bin\idea64.exe"],
            ["sublime", "C:\Program Files\Sublime Text\sublime_text.exe"]]

    say("Hi, I am FRIDAY A.I.")
    while True:
        print("I am listening...")
        query = takeCommand()
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Sir...")
                webbrowser.open(site[1])

        if f"Play music".lower() in query.lower():
            say(f"Playing music sir...")
            musicPath = "D:\STUDY\PYTHON\song.mp3"
            os.system(f"start {musicPath}")
            # playMusic(musicPath)
            time.sleep(30)

        if f"the time" in query.lower():
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {strfTime}")

        for app in apps:
            if f"Open {app[0]}".lower() in query.lower():
                say(f"Opening {app[0]} Sir...")
                os.system(f"start {app[1]}")


    # say(text)
