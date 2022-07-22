from asyncio import subprocess
from click import command as cd
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import subprocess
from datetime import *


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                print(command)
    except:
        pass
    return command
    
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        today = date.today()
        print(today)
        talk(today) 
        
    elif 'open' in command:
        if 'calculator' in command:
            subprocess.call('calc.exe')   
        if 'notepad' in command:
            subprocess.call('Notepad.exe')    
        if 'youtube' in command:
            # subprocess.call('')     
            webbrowser.open('https://www.youtube.com')
   
    
    elif 'do'in command and 'homework' in command:
        talk('Sorry, I''m busy')
  
    elif 'search' in command:
        talk('Searching for ' + command.split('search')[1])
        url = 'https://google.com/search?q=' + command.split('search')[1]
        try:
            webbrowser.get().open(url)
            talk('This is what I found .')
        except:
            talk('Please check your Internet')

    elif 'locate' in command or 'location' in command:
        talk('Which place are you looking for ?')
        temp_audio = take_command()
        # app.eel.addUserMsg(temp_audio)
        talk('Locating...')
        url = 'https://google.nl/maps/place/' + temp_audio + '/&amp;'
        try:
            webbrowser.get().open(url)
            talk('This is what I found Sir')
        except:
            talk('Please check your Internet')

    
    
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)    
    elif('what is' in command):
        if ('multiply' in command or 'x' in command):
            command=command.replace('multiply', "*")
            command =command.replace('x',"*")
            command = command.split('what is ')[1]
            print(command)
            print(eval(command))    
            talk(eval(command))
            exit()
        else:
            command = command.split('what is ')[1]
            print(command)
            print(eval(command))    
            talk(eval(command))
    # elif 'what are' in command :
    #     person = command.replace('what ', '')
    #     info = wikipedia.summary(person, 1)
    #     print(info)
    #     talk(info)  
    elif('stop' in command):
        print(command)
        print("Shutting down!!")
        talk("Shutting down!!")
        exit()     
    else:
        talk('Please say the command again.')


while True:
    run_alexa()