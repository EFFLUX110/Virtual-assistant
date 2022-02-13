import time
print('\033[1m'+'\n\n P L E A S E  W A I T  F O R  S O M E T I M E  \n' + "\033[0m")
time.sleep(3)
print('\033[1m'+'\n\n D O W N L O A D I N G  P A C K A G E S  . . . \n\n' + "\033[0m")
time.sleep(2)
import os

os.system('pip install stdiomask')
os.system('pip install pyttsx3')
os.system('pip install wikipedia')
os.system('pip install speedtest-cli')
os.system('pip install beautifulsoup4')
os.system('pip install requests')
os.system('pip install pygame')

import pyttsx3                       
from datetime import datetime,date
import wikipedia
import random
import webbrowser
import speedtest
from bs4 import BeautifulSoup
import json
import requests                 
import stdiomask

from os import environ                            
# This method is used just to remove default welcome message from pygame
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
    music_list=['Alan Walker  Fade NCS Release.mp3','Alan Walker  Spectre NCS Release.mp3','Tobu  Itro  Sunburst NCS Release.mp3','OnlyMP3.net - Excuses  AP Dhillon  Gurinder Gill  Intense  Banger SZN-vX2cDW8LUWk-192k-1632771183696.mp3']
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

    print("I am EFFLUX , Virtual assistant "
          "Created by Mrinank Bhowmick and Aditya Prasad,"
          "I can help you in various regards,"
          "I can search for you on the Internet,"
          "I can also grab definitions for you from wikipedia,"
          "I am always happy to help you!")

    speak("I am EFFLUX , Virtual assistant "
          "Created by Mrinank Bhowmick and Aditya Prasad,"
          "I can help you in various regards,"
          "I can search for you on the Internet,"
          "I can also grab definitions for you from wikipedia,"
          "I am always happy to help you!")

def quote_func(type):
    try:

        response=requests.get(f"https://efflux.herokuapp.com/{type}")
        json_data=json.loads(response.text)
        quote =json_data['q'] + " by "+json_data["a"]
        return quote

    except:
        pass

########################## MAIN ############################

if __name__ == "__main__":

    wishMe()

    while True:
        Input_command=input('Query : ').lower()

        ########################## Introduction ############################
        
        if 'tell me about yourself' in Input_command or 'who are you' in Input_command:
            Introduction()

        #################### WIKIPEDIA ##############################

        elif "wikipedia"in Input_command:
            #Tell ---> sachin tendulkar wikipedia
            try:
                print('searching wikipedia....')
                speak('searching wikipedia....')
                results=wikipedia.summary(Input_command.replace("wikipedia", ""), sentences=2)
                print(results)
                speak(results)
            except Exception as e:
                print(e)

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
        
        elif "open stack overflow" in Input_command:
            print('opening stack overflow for u')
            speak('opening stack overflow for u')
            webbrowser.open("stack overflow.com")
        
        elif "open twitch" in Input_command:
            print('opening twitch for u')
            speak('opening twitch for u')
            webbrowser.open("twitch.tv")
        
        ########################### GAMES ###########################

        elif "tic tac toe" in Input_command:
            #Request ---> I want to play tic tac toe

            import tictactoe
            tictactoe.play_game()

        elif "internet" in Input_command or "speed" in Input_command:
            speak("Wait for while...")
            st = speedtest.Speedtest()
            up = round(st.upload() / 10 ** 6, 2)
            down = round(st.download() / 10 ** 6, 3)

            print(f"Download Speed is {down} MB/s")
            speak(f"Download Speed is {down} MB per Sceond")

            print(f"Upload Speed is {up} MB/s")
            speak(f"Upload Speed is {up} Mb per Sceond")

        elif 'joke' in Input_command:
            #Ask --> Tell me a joke
            fin=open("jokes.txt",'r')
            joke=fin.readlines()[random.randint(1,37)]
            print(joke)
            speak(joke)
            fin.close()

        elif "weather" in Input_command:
            #Ask ---> what is today's weather

            search='temperature in kolkata'
            url=f'https://www.google.com/search?q={search}'
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser") 
            temp = data.find("div",class_="BNeawe").text
            print(f"current {search} is {temp}")
                         
        ########################### NOTE #############################

        elif "write a note" in Input_command:
            #Request ---> Can you do me a favour, can you write a note for me

            speak("What should i write, sir")
            note = input("Tell me what to write:\n")
            file = open('notes.txt', 'a')

            speak("Sir, Should I include date ?")
            print("Sir, Should I include date ?")
            snfm = input("yes/no ")

            if 'yes' in snfm or 'sure' in snfm:
                strTime = str(date.today())
                file.write(strTime)
                file.write(" :- ")
                file.write(f'{note}\n')
                file.close()

            else:
                file.write(f'{note}\n') 
                file.close()

        elif "show note" in Input_command or "see note" in Input_command:
            #Request ---> I want to see notes
            # or request ---> show me the notes

            speak("Showing notes on terminal.")
            file = open("notes.txt", "r")
            print(file.read())
        
        ############### CURRENT TIME ###############

        elif "tell time" in Input_command or "what is the time" in Input_command:
            #Ask ---> Can you tell what is the time right now?

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Current Time is", current_time)
            speak(f"Current Time is {current_time}")
        
        ############### COVID CASES ################

        elif 'active cases of covid' in Input_command:
            #Ask ---> active cases of covid in India
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
            #Ask---> Tell me today's date

            today = date.today()
            print("Today's date:", today)
            speak(f"Today's date: {today}")

        ################ YOUTUBE SEARCH #############

        elif 'youtube' in Input_command:    
            # Ask ---> Search for Avengers on Youtube

            search_term = Input_command.split('for')[-1].split('on')[0].strip()
            url = f'https://www.youtube.com/results?search_query={search_term}'
            webbrowser.get().open(url)
            speak(f'Here is what I found for {search_term} on youtube')

        ################# QUOTES ################

        elif "depressed" in Input_command or "motivate" in Input_command:

            fin=open("quotes.txt",'r')
            quote=fin.readlines()[random.randint(1,200)]
            print(quote)
            speak(quote)
            fin.close()
        
        elif "add quote" in Input_command:
            #Tell ---> I want to add quote

            password=stdiomask.getpass("Only admin have write access to it \nEnter password: ")
            
            if password == "admin":
                print("Login successful")
                fin=open("quotes.txt",'a')
                Quote=input("please tell which quote you want to add: ")
                author=input("who is the author of this quote: ")
                fin.write(f'{quote} by {author}\n')
                fin.close()

        elif "business quote" in Input_command:

            quote=quote_func('business')
            print(quote)
            speak(quote)
        
        elif "war quote" in Input_command:

            quote=quote_func('war')
            print(quote)
            speak(quote)
        
        elif "love quote" in Input_command:

            quote=quote_func('love')
            print(quote)
            speak(quote)
        
        elif "life quote" in Input_command:

            quote=quote_func('life')
            print(quote)
            speak(quote)
        
        elif "hustle quote" in Input_command:

            quote=quote_func('hustle')
            print(quote)
            speak(quote)
        
        elif "friendship quote" in Input_command:

            quote=quote_func('friendship')
            print(quote)
            speak(quote)

        ############### BYE ####################

        elif "bye" in Input_command:

            speak("Bye for now...stay safe , stay happy , stay healthy")
            exit()