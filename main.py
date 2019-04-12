import speech_recognition as sr
import webbrowser
import os
from termcolor import colored
import subprocess
import random
import sys
import requests
from random import choice
import pyttsx3
engine = pyttsx3.init()
def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())

print()
print()
print()
name = str(input(colored("What's your name? ", "green")))
print()
print()
print()
def main():
	while True:
		r = sr.Recognizer()
		how_are_you_answers = ["I'm fine thanks!", "I'm good", "I'm feeling very good today!", "Hi, I'm fine!"]
		hi_q = ["Hi!", "Hello", "hi", "Hi there!", "Hi there", "Hi how are you?", "Hi what's up?"]

		ans1 = choice(how_are_you_answers)
		ans2 = choice(hi_q)

		with sr.Microphone() as source:
			print(colored("Say anything: ", "blue"))
			audio = r.listen(source)

		try:
			text = r.recognize_google(audio)

			if text == "ehi john" or text == "ei John" or text == "hey John" or text == "hey john":
				engine.say("Yeeesss", name)
				engine.runAndWait()
			elif text == "hi" or text == "hai" or text == "hi Jon" or text == "hi John":
				engine.say(ans2)
				engine.runAndWait()
				if text == "i'm fine" or text == "i'm fine thanks" or text == "I'm fine" or text == "i'm fine" or text == "i'm good thanks":
					engine.say("I'm happy you are fine!")
					engine.runAndWait()
				elif text == "i'm fine and you" or text == "fine and you" or text == "i'm good and you" or text == "i'm fine and you":
					engine.say("I'm fine!")
			elif text == "how are you" or text == "how are you feeling" or text == "hi how are you" or text == "hello John how are you" or text == "hi John how are you you":
				engine.say("I'm fine thanks")
				engine.runAndWait()
			elif text == "open YouTube" or text == "open youtube" or text == "can you open youtube":
				website = "https://www.youtube.com"
				webbrowser.open_new_tab(website)
				engine.say("Sure")
				engine.runAndWait()
			elif text == "open Google" or text == "open google" or text == "can you open google":
				website = "https://www.google.com"
				webbrowser.open_new_tab(website)
				engine.say("Sure", name)
				engine.runAndWait()
			elif text == "open gmail" or text == "open gimail" or text == "open Gmail" or text == "can you open Gmail":
				website = "https://mail.google.com/mail/u/0/"
				webbrowser.open_new_tab(website)
				engine.say("Sure")
				engine.runAndWait()
			elif text == "open instagram" or text == "open Instagram" or text == "can you open Instagram":
				website = "https://www.instagram.com/"
				webbrowser.open_new_tab(website)
				engine.say("Sure")
				engine.runAndWait()
			elif text == "open whatsapp" or text == "open what's app" or text == "open whats app" or text == "open WhatsApp" or text == "can you open WhatsApp":
				website = "https://web.whatsapp.com/"
				webbrowser.open_new_tab(website)
				engine.say("Sure")
				engine.runAndWait()
			elif text == "open latin dictionary" or text == "open Latin's dictionary" or text == "open Latin dictionary" or text == "open late dictionary" or text == "open late in dictionary":
				website = "https://www.dizionario-latino.com/"
				webbrowser.open_new_tab(website)
				engine.say("Sure")
				engine.runAndWait()
			elif text == "open git hub" or text == "open GitHub" or text == "open github" or text == "open git ab" or text == "open gitab":
				website = "https://github.com/"
				webbrowser.open_new_tab(website)
				engine.say("Sure")
				engine.runAndWait()
			elif text == "thanks" or text == "thank you" or text == "appreciate it" or text == "thanks bro":
				engine.say("you are welcome", name)
				engine.runAndWait()
			elif text == "what's your name" or text == "what is your name" :
				engine.say("My name is John. I was programmed, by Alex Foderaro. you can follow him on Instagram if you want.")
				engine.runAndWait()
			elif text == "sing a song":
				engine.say("Only wear designer, esskeetit. Hoppin' out the Wraith, esskeetit Smashin' on your bitch, esskeetit Runnin' up a check with no limit.Poppin' on X, poppin' on XPoppin' on X, pills (yuh, X)Got a new car, got a new bitch  yeah And I got a new deal")
				engine.runAndWait()
			elif text == "what's my name" or text == "what is my name" :
				engine.say(name)
				engine.runAndWait()
			elif text == "set an alarm" or text == "set me an alarm" or text == "can you set me an alarm" or text == "set an alarm for me":
				engine.say("Opening the alarm", name)
				engine.runAndWait()
				os.system('python3 alarm.py')
			elif text == "quit" or text == "Quit" or text == "exit" or text == "Exit":
				quit()
				engine.say("Ok")
				engine.runAndWait()
			print()
			print()
			print()
			print(colored("You said: {}".format(text), "yellow"))
			print()
			print()
			print()
		except:
			if text == "quit" or text == "Quit" or text == "exit" or text == "Exit":
				quit()
			icantUndersatand = colored("Sorry! I can't understand", "red")
			print(icantUndersatand, name)

main()