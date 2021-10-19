import pyttsx3                                #install
from datetime import datetime,date
import wikipedia                                #insta
import psutil
import time
import random
import webbrowser
import speedtest
from bs4 import BeautifulSoup 
from GoogleNews import GoogleNews
import nltk
from textblob import TextBlob
from newspaper import Article
import json
import requests                                #instal

from os import environ                             # This method is used just to remove default welcome message from pygame
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
pygame.mixer.init()
pygame.init()

engine=pyttsx3.init()    
voices = engine.getProperty('voices')

########################### BANNER #####################################
 
print('───────────▄▄▄▄▄▄▄▄▄───────────')
time.sleep(0.1)
print('────────▄█████████████▄────────      ███████╗███████╗███████╗██╗     ██╗   ██╗██╗  ██╗')
time.sleep(0.1)
print('█████──█████████████████──█████      ██╔════╝██╔════╝██╔════╝██║     ██║   ██║╚██╗██╔╝')
time.sleep(0.1)
print('▐████▌─▀███▄───────▄███▀─▐████▌      █████╗  █████╗  █████╗  ██║     ██║   ██║ ╚███╔╝')
time.sleep(0.1)
print('─█████▄──▀███▄───▄███▀──▄█████─      ██╔══╝  ██╔══╝  ██╔══╝  ██║     ██║   ██║ ██╔██╗')
time.sleep(0.1)
print('─▐██▀███▄──▀███▄███▀──▄███▀██▌─      ███████╗██║     ██║     ███████╗╚██████╔╝██╔╝ ██╗')
time.sleep(0.1)
print('──███▄▀███▄──▀███▀──▄███▀▄███──      ╚══════╝╚═╝     ╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝')
time.sleep(0.1)
print('──▐█▄▀█▄▀███─▄─▀─▄─███▀▄█▀▄█▌──')
time.sleep(0.1)
print('───███▄▀█▄██─██▄██─██▄█▀▄███───                     Virtual Assistant')
time.sleep(0.1)
print('────▀███▄▀██─█████─██▀▄███▀────')
time.sleep(0.1)
print('───█▄─▀█████─█████─█████▀─▄█───')
time.sleep(0.1)
print('───███────────███────────███───')
time.sleep(0.1)
print('───███▄────▄█─███─█▄────▄███───')
time.sleep(0.1)
print('───█████─▄███─███─███▄─█████───')
time.sleep(0.1)
print('───█████─████─███─████─█████───')
time.sleep(0.1)
print('───█████─████─███─████─█████───')
time.sleep(0.1)
print('───█████─████─███─████─█████───')
time.sleep(0.1)
print('───█████─████▄▄▄▄▄████─█████───')
time.sleep(0.1)
print('────▀███─█████████████─███▀────')
time.sleep(0.1)
print('──────▀█─███─▄▄▄▄▄─███─█▀──────')
time.sleep(0.1)
print('─────────▀█▌▐█████▌▐█▀─────────')
time.sleep(0.1)
print('────────────███████────────────')
print()
print()

def speak(audio):
    engine.setProperty("rate", 150)
    engine.setProperty('voice',voices[1].id)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour =  int(datetime.now().hour)
    if hour >=0 and hour<12:
        print("good morning",end=' ')
        speak('good morning')
    elif hour>=12 and hour<18:
        print("good afternoon",end=' ')
        speak('good afternoon') 
    else:
        print("good evening")
        speak('good evening')

    print("I am efflux")
    print("Please tell me how may I help you")
    speak('I am ef lux')
    speak('Please tell me how may I help you')

def playmusic(): 
    music_list=['Alan Walker  Fade NCS Release.mp3','Alan Walker  Spectre NCS Release.mp3','Tobu  Itro  Sunburst NCS Release.mp3']
    music=random.choice(music_list)
    pygame.mixer.music.load(music)
    pygame.mixer.music.play()

def stopmusic(): 
    pygame.mixer.music.stop()

def check_command_is_for_covid_cases(command):
    country = get_country(command).capitalize()
    cases = get_covid_cases(country)
    return (f"The current active cases in {country} are {cases}")


def get_country(command):                   # For getting only the country name for the whole query
    country = command.split()[-1]
    if country == "?":
        country = command.split()[-2]
    return country


def get_covid_cases(country):               # For getting current covid cases
    totalActiveCases = 0
    response = requests.get('https://api.covid19api.com/live/country/' + country + '/status/confirmed').json()
    for data in response:
        totalActiveCases += data.get('Active')
    return totalActiveCases

def Introduction():
    print("I am EFFLUX , Virtual assistant"
          "Created by Mrinank Bhowmick and Aditya Prasad,"
          "I can help you in various regards,"
          "I can search for you on the Internet,"
          "I can also grab definitions for you from wikipedia,"
          "I am always happy to help you!")

    speak("I am EFFLUX , Virtual assistant"
          "Created by Mrinank Bhowmick and Aditya Prasad,"
          "I can help you in various regards,"
          "I can search for you on the Internet,"
          "I can also grab definitions for you from wikipedia,"
          "I am always happy to help you!")

def quote(type):
    try:
        response=requests.get(f"https://efflux.herokuapp.com/{type}")
        json_data=json.loads(response.text)
        quote =json_data['q'] + " by "+json_data["a"]
        return quote
    except:
        pass

if __name__ == "__main__":

    wishMe()

    while True:
        Input_command=input('query ').lower()
        
        #################### WIKIPEDIA ##############################

        if "wikipedia"in Input_command:

            print('searching wikipedia....')
            speak('searching wikipedia....')
            results=wikipedia.summary(Input_command.replace("wikipedia", ""), sentences=2)
            print(results)
            speak(results)

        ########################## Introduction ############################
        
        elif 'tell me about yourself' and 'who are you' in Input_command:
            Introduction()

        ############################ MUSIC ###############################

        elif "play music" in Input_command:
            playmusic()

        elif "stop music" in Input_command:
            stopmusic()

        ############################## SEARCH ON WEB #####################

        elif "open youtube" in Input_command:
            print('opening youtube for u')
            speak('opening youtube for u')
            webbrowser.open("youtube.com")

        elif "open google" in Input_command:
            print('opening google for u')
            speak('opening google for u')
            webbrowser.open("google.com")
        
        ########################### GAMES ###########################

        elif "ttc" in Input_command:
            import tictactoe
            tictactoe.play_game()

        elif 'power left' in Input_command or 'battery' in Input_command or "power" in Input_command:
            # Works only in laptop
            battery=psutil.sensors_battery()
            percentage =int(battery.percent)
            print(percentage)
            speak(f"sir our system have {percentage} percent battery")
            if percentage>=75:
                speak('we have enough power to continue our work')
            elif percentage>=40 and percentage<=75:
                speak( ' we should connect our system to charging point ')
            else:
                speak('we have very low power')

        elif "internet" in Input_command and "speed" in Input_command:
            speak("Wait for while...")
            st = speedtest.Speedtest()
            up = round(st.upload() / 10 ** 6, 2)
            down = round(st.download() / 10 ** 6, 2)
            print(f"Download Speed is {down} MB/s")
            speak(f"Download Speed is {down} MB per Sceond")
            print(f"Upload Speed is {up} MB/s")
            speak(f"Upload Speed is {up} Mb per Sceond")

        elif 'joke' in Input_command:
            import pyjokes
            s=pyjokes.get_joke()
            print(s)
            speak(s)

        elif "weather" in Input_command:
            search='temperature in kolkata'
            url=f'https://www.google.com/search?q={search}'
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser") 
            temp = data.find("div",class_="BNeawe").text
            print(f"current {search} is {temp}")
                         
        ########################### NOTE #############################

        elif "write a note" in Input_command:
            speak("What should i write, sir")
            note = input("Tell what to write:\n")
            file = open('notes.txt', 'a')
            speak("Sir, Should i include date ?")
            print("Sir, Should i include date ?")
            snfm = input("yes/no ")
            if 'yes' in snfm or 'sure' in snfm:
                strTime = str(today = date.today())
                file.write(strTime)
                file.write(" :- ")
                file.write(f'{note}\n')
                file.close()
            else:
                file.write(f'{note}\n') 
                file.close()

        elif "show note" in Input_command:
            speak("Showing notes on terminal.")
            file = open("notes.txt", "r")
            print(file.read())
        
        ############### CURRENT TIME ###############

        elif "tell time" in Input_command or "what is the time" in Input_command:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Current Time is", current_time)
            speak("Current Time is", current_time)
        
        ############### COVID CASES ################

        elif 'active cases of covid' in Input_command:
            # Sample--> active cases of covid in india
            cases=check_command_is_for_covid_cases(Input_command)
            print(cases)
            speak(cases)

        ############### DAY ######################

        elif 'which day is today' in Input_command:
            day = datetime.today().weekday() + 1
            Day_dict = {1: 'Monday', 2: 'Tuesday',3: 'Wednesday', 4: 'Thursday',5: 'Friday', 6: 'Saturday',7: 'Sunday'}

            if day in Day_dict.keys():
                day_of_the_week = Day_dict[day]

                print(day_of_the_week)
                speak(f"The day is {day_of_the_week}")

        ############### DATE ######################

        elif 'date' in Input_command:

            today = date.today()
            print("Today's date:", today)
            speak(f"Today's date: {today}")

        ################ YOUTUBE SEARCH #############

        elif 'youtube' in Input_command:    # Ask ---> Search for Avengers on Youtube
            search_term = Input_command.split('for')[-1].split('on')[0].strip()
            url = f'https://www.youtube.com/results?search_query={search_term}'
            webbrowser.get().open(url)
            speak(f'Here is what I found for {search_term} on youtube')

        ################# QUOTES ################

        elif "depressed" in Input_command or "motivate" in Input_command:
            fin=open("quotes.txt",'r')
            quote=fin.readlines()[random.randint(1,200)]
            print(quote)

        elif "business quote" in Input_command:
            quote=quote('business')
            print(quote)
            speak(quote)
        
        elif "war quote" in Input_command:
            quote=quote('war')
            print(quote)
            speak(quote)
        
        elif "love quote" in Input_command:
            quote=quote('love')
            print(quote)
            speak(quote)
        
        elif "life quote" in Input_command:
            quote=quote('life')
            print(quote)
            speak(quote)
        
        elif "hustle quote" in Input_command:
            quote=quote('hustle')
            print(quote)
            speak(quote)
        
        elif "friendship quote" in Input_command:
            quote=quote('friendship')
            print(quote)
            speak(quote)

        ############### BYE ####################

        elif "bye" in Input_command:
            speak("Bye for now...stay safe , stay happy , stay healthy")
            exit()