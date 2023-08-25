import time
import webbrowser
import speech_recognition as sr
import win32com.client
import subprocess
import platform
import pygame

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

speaker = win32com.client.Dispatch("SAPI.SpVoice")


def say(text):
    speaker.Speak(text)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 0.8       by default 0.8, can change
        audio = r.listen(source)
        try:
            print("Recognising")
            user_query = r.recognize_google(audio, language="en-in")
            print(f"User said: {user_query}")
            return user_query
        except Exception as e:
            return "Sorry, please speak again."


def playMusic(file_path):
    if platform.system() == 'Darwin':
        subprocess.run(['afplay', file_path])
    elif platform.system() == 'Windows':
        subprocess.run(['start', '/b', 'KMPlayer64', file_path], shell=True)
    elif platform.system() == 'Linux':
        subprocess.run(['aplay', file_path])
    else:
        print("Unsupported platform.")


if __name__ == '__main__':
    # print("Enter what you want me to speak")
    # s = input()
    sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"],
             ["google", "https://google.com"], ["github", "https://github.com"], ["youtube", "https://youtube.com"]]

    say("Hi, I am FRIDAY A.I.")
    while True:
        print("I am listening...")
        # query = takeCommand()
        # for site in sites:
        #     if f"Open {site[0]}".lower() in query.lower():
        #         say(f"Opening {site[0]} Sir...")
        #         webbrowser.open(site[1])
        #
        #     if f"Play music".lower() in query.lower():
                say(f"Playing music sir...")
                musicPath = "D:\STUDY\PYTHON\song.mp3"
                # os.system(f"open {musicPath}")
                playMusic(musicPath)
                time.sleep(30)

        # say(text)
