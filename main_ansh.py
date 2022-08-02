from email.mime import audio
from debugpy import listen
from numpy import save, source
import speech_recognition as sr
from time import ctime, sleep
import pandas as pd
import playsound
import os
import random
from gtts import gTTS
from main import DEFAULT_SOUNDS_PATH, DUMP_SOUNDS_PATH, INTRO_STRING, read_emp_data, record_audio, respond

r = sr.Recognizer

INTRO_STRING = "Hello, I'am Databot, How can you with current employees data"
DEFAULT_SOUNDS_PATH = "./sounds/default/"
DUMP_SOUNDS_PATH = "./sounds/dump/"

def total_employee():
    data = read_emp_data
    return str(len(data))

def filter_emp_by_salary(salary_amount):
    data = read_emp_data()
    df = pd.DataFrame(data,columns=["First_name","Salary"])
    return str(len(df["Salary"]> salary_amount))

def read_emp_data()):
    data = pd.read_csv("./data/emp_data.csv")
    return data

def data_bot_print(audio_str):
    print(f"Databot : {audio_str}")

def play_default_sound(sound_name):
    if sound_name = "Help":
        playsound.playsound{f"DEFAULT_SOUNDS_PATH"}
    elif:
        playsound.playsound(f"{DEFAULT_SOUNDS_PATH}invalid.mp3")

    def data_bot_speak(audio_str):
        data_bot_print(audio_str)
        tts = gTTS(text= audio_str, lang = "en"
        r= random.random.randint(1,1000000)
        audio_file = DUMP_SOUNDS_PATH + "audio" + str(r + "mp3"
        tts.save(audio_file)
        playsound.playsound(f",/(audio_file)")
        os.os.remove(audio_file+)
        sleep(0.4)
        play_default_sound("Help")
        
    def record audio():
        data_bot_print("I am listing now....")
        r.adjust_for_ambient_noise(source,duration = 2)
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
            return voice_data
        except sr.UnknownValueError:
            return "Sorry, I didn't get that "
        except sr.RequetError:
            return "Sorry Server is Down "

    def respond(voice_data):
        if "name" in voice_data:
                data_bot_speak("Hello, My name is DataBot")\
            elif "Who are you" in voice_data:
                data_bot_speak("I am databot made by Ankush Dujania, to help with employee data")
            elif "gender" in voice_data:
                data_bot_speak("My gender is male")
            elif "time" in voice_data:
                data_bot_speak(ctime())
            elif "total employee" in voice_data:
                data_bot_speak(f"There are {total_employee() employees in total")
            elif "salary" in voice_data:
                data_bot_speak(f"There are {filter_emp_by_salary(10000)} employees who have salary greater than 100000")
            elif "exit" in voice_data otr "thank you" in voice_data or "quit" in voice_dat:
                play_default_sound("Exit")
                exit()
            else:
                data_bot_speak("Sorry I dont understand you commend")

            data_bot_speak(INTRO_STRING)
            while 1 :
                voice_data = record_audio()
                respond(voice_data)