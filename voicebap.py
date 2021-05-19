import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import smtplib
import json
import requests
import cv2
import pygame
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from ecapture import ecapture as ec



#---------------------------Setting up the speech engine---------
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('n160003@rguktn.ac.in', "BashaMunvar90")
    server.sendmail('n160003@rguktn.ac.in', to, content)
    server.close()


def search_web(input):
    options = Options()
    options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\\Users\\sunka\\Documents\\chromedriver.exe')

    if 'youtube' in input.lower():

        speak("Opening in youtube")
        indx = input.lower().split().index('youtube')
        query = input.split()[indx + 1:]
        driver.get("http://www.youtube.com/results?q=" + '+'.join(query))
        return

    elif 'wikipedia' in input.lower():

        speak("Opening Wikipedia")
        indx = input.lower().split().index('wikipedia')
        query = input.split()[indx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return

    else:

        if 'google' in input:

            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))

        elif 'search' in input:

            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))

        else:

            driver.get("https://www.google.com/search?q =" + '+'.join(input.split()))

        return
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)
        print("Done Recording...!")

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


def open_application(input):
    if "chrome" in input:
        speak("Google Chrome")
        os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
        return

    elif "word" in input:
        speak("Opening Microsoft Word")
        os.startfile('C:\\Program Files (x86)\\Microsoft Office\\Office12\\WINWORD.exe')
        return

    elif "powerpoint" in input:
        speak("Opening Microsoft Word")
        os.startfile('C:\\Program Files (x86)\\Microsoft Office\\Office12\\POWERPNT')
        return

    elif "excel" in input:
        speak("Opening Microsoft Excel")
        os.startfile('C:\\Program Files (x86)\\Microsoft Office\\Office12\\EXCEL.exe')
        return
    elif "calculator" in input:
        speak("Opening Calculator")
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')

    else:

        speak("Application not available")
        return


# Method to self shut down system
def quitSelf():
    speak("do u want to switch off the computer sir")

    # Input voice command
    take = takeCommand()
    choice = take
    if choice == 'yes':
        # Shutting down
        print("Shutting down the computer")
        speak("Shutting the computer")
        os.system("shutdown /s /t 30")
    if choice == 'no':
        # Idle
        print("Thank u sir")
        speak("Thank u sir")

def Music():
    pygame.init()
    display = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("sound demo")
    pygame.mixer.music.load("C:\\Users\\sunka\\Music\\[iSongs.info] 02 - Kadale Vidichi.mp3")
    soun_obj = pygame.mixer.Sound("C:\\Users\\sunka\\Music\\[iSongs.info] 02 - Kadale Vidichi.mp3")
    pygame.mixer.music.play()
    soun_obj.play()
    while True:
        for eve in pygame.event.get():
            comand = takeCommand().lower()
            if eve.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
if __name__=='__main__':

    wishMe()
    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant G-one is shutting down,Good bye')
            print('your personal assistant G-one is shutting down,Good bye')
            break


        if "find" in statement or "play" in statement:
            search_web(statement)
        elif "shutdown" in statement:
            quitSelf()

        elif 'open' in statement:
            open_application(statement)

        elif 'open calculator' in statement:
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')


        elif ("note" in statement) or ("notes" in statement) or ("notepad" in statement) or ("editor" in statement) or ("9" in statement):
            speak("Opening")
            speak("notepad")
            print(".")
            print(".")
            os.system("Notepad")

        elif ("ie" in statement) or ("msedge" in statement) or ("edge" in statement) or ("8" in statement):
            speak("Opening")
            speak("MICROSOFT EDGE")
            print(".")
            print(".")
            subprocess.Popen(["C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"])

        elif ("vlcplayer" in statement) or ("player" in statement) or ("video player" in statement) or ("5" in statement):
            speak("Opening")
            speak("VLC PLAYER")
            print(".")
            print(".")
            subprocess.Popen(["C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"])
        elif "who are you" in statement or "define yourself" in statement:
            text = '''Hello, I am Person. Your personal Assistant.
                    I am here to make your life easier. You can command me to perform
                    various tasks such as  opening applications etcetra'''
            speak(text)

        elif "who made you" in statement or "created you" in statement:
            text = '''I have been created by Mallikharjuna 
             Basha 
             Prasanna 
             Leekeetaaa
             Nokaraj'''

            speak(text)

        elif 'play music' in statement:
            Music()
            time.sleep(5)
        elif 'email to sunkara' in statement:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sunkaramallikharjuna90@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")
        elif 'open stackoverflow' in statement:
            webbrowser.open("stackoverflow.com")
        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif "camera" in statement:
            videoCaptureObject = cv2.VideoCapture(0,cv2.CAP_DSHOW)
            result = True
            while(result):
            	ret,frame = videoCaptureObject.read()
            	cv2.imwrite("image1.jpg",frame)
            	result = False
            videoCaptureObject.release()
            cv2.destroyAllWindows()

        


