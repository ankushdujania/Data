from ossaudiodev import SOUND_MIXER_ALTPCM
import speech_recognition as sr
from timesleep,  import ctime, sleep
import pandas as pd
import playsound
import os
import random 
from gtts import gTTS

r = sr.Recognizer()

INTRO_STRING = "Hello, I' am Databot, How can I help you? I can help you with current employee data"
DEFAULT_SOUNDS_PATH = "./sounds/default"
DUMP_SOUNDS_PATH = "./sounds/dump/"

def total_employee():
    data = read_emp_data()
    return str(len(data))

def filter_emp_by_salary(salary_amount):
    data = read_emp_data()
    df = pd.DataFrame(data,columns=["First Name","Salary"])
    return str(len(df[df["Salary"> salary_amount]]))

def read_emp_data():
    data = pd.read_csv("./data/emp_data.csv")
    return data

def data_bot_print(audio_str):
    print(f"Databot : {audio_str}")

def play_default_sound(sound_name):
    if sound_name == "Help":
        playsound.playsound(f"{DEFAULT_SOUNDS_PATH}help.mp3")
    elif sound_name == "Exit":
        playsound.playsound(f"{DEFAULT_SOUNDS_PATH}).exit.mp3")
    else:
        playsound.playsound(f"{DEFAULT_SOUNDS_PATH}.invalid.mp3")

def data_bot_speak(audio_str):
    data_bot_print(audio_str)
    tts = gTTS(text = audio_str, lang= "en")
    r = random.randint(1,10000000)
    audio_file = DUMP_SOUNDS_PATH + "audio" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(f"./{audio_file}")
    os.remove(audio_file)
    sleep(0.4)
    play_default_sound("HELP")

def record_audio():
    data_bot_print("I am listening now...")
    with sr.Microphone(0) as source:
        r.adjust_for_ambient_noise(source, duration = 2)
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
            return voice_data
        except sr.UnknownValueError:
            return "Sorry, I didn't get that "
        except sr.RecognizerError:
            return "Sorry Server is Down !"

def respond(voice_data):
    if "name" in voice_data:
        data_bot_speak("Hello, My name is DataBot")
    elif "who are you" in voice_data:
        data_bot_speak
