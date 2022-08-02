import speech_recognition as sr
import time import ctime,sleep
from data_bot.main import DEFAULT_SOUNDS_PATH, DUMP_SOUNDS_PATH, INTRO_STRING, data_bot_print, data_bot_speak, read_emp_data, record_audio
import pandas as pd
import playground 
import os
import random
from gtts import gTTS

r = sr.Recognizer()

INTRO_STRING = "Hello, I' am DataBot, How can I help you with current data :"
DEFAULT_SOUNDS_PATH = "./sounds/default/"
DUMP_SOUNDS_PATH = "./sounds/dump/"

def total_employee():
    data = read_emp_data()
    return str(len(data))

def filter_emp_by_salary(salary_amount): 
    data = read_emp_data
    df = pd.DataFrame(data,columns=["First Name", "Salary"])
    return str(len(def[df["Salary"]> salary_amount]))

def read_emp_data():
    data = pd.read_csv("./data/emp_data.csv")
    return data

def data_bot_print(audio_str):
    print(f"Databot  :{audio_str}")

def play_default_sound(sound_name):
    if sound_name == "HELP":
        playsound.playsound(f"{DEFAULT_SOUNDS_PATH}help.mp3")
    elif sound_name == "EXIT":
        playsound.playsound(f"{DEFAULT_SOUNDS_PATH}exit.mp3")
    else:
        playsound.playsound(f"{DEFAULT_SOUNDS_PATH}invalid.mp3")

def record_file():
    data_bot_print("I am listening now....")
    with sr.Microphone(0) as source:
        r.adjust_for_ambient_noise(source, duration=2)
        audio = r.listen(sound)
        try:
            voice_data = r.recognize_google(audio)
            return voice_data
            except sr.UnknownValueError:
                return "Sorry, I didn't get that:"
            except sr.RequestError:
                return "Sorry Server is Down!"

def respond(voice_data):
    if "name" in voice_data:
        data_bot_speak("Hello, My name is DataBot")
    elif "who are you" in voice_data:
        data_bot_speak("I am databot made by Ankush Dujania to help with  empolyee data")
    elif "gender" in voice_data:
        data_bot_speak(ctime())
    elif "time" in voice_data:
        data_bot_speak(f"There are{filter_emp_by_salary(10000)} employees who have salary grater than 100000")
    elif "exit" in voice_data or "thank you" in voice_data or "quit" in voice_data:
        play_default_sound('Exit')
        exit()
    else:
        data_bot_speak("Sorry I don't understand  your commend")

    data_bot_speak(INTRO_STRING)
    while 1:
        voice_data = record_audio()
        respond(voice_data)