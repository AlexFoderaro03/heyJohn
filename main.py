import speech_recognition as sr
import webbrowser
import subprocess
import random
import sys
import requests
from google import search
from random import choice
import pyttsx3
engine = pyttsx3.init()


def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())
'''
IS_WINDOWS = sys.platform.lower() == "win32"

if IS_WINDOWS:
	r = sr.Recognizer()
	how_are_you_answers = ["I'm fine thanks!", "I'm good", "I'm feeling very good today!", "Hi, I'm fine!"]
	ans1 = choice(how_are_you_answers)

	with sr.Microphone() as source:
		print("Say anithing: ")
		audio = r.listen(source)

	try:
		text = r.recognize_google(audio)
		file1 = open("./conversation.txt", "w")
		file1.write(text)
		file1.close

		if text == "ehi john" or text == "ei John" or text == "hey John" or text == "hey john":
			engine.say("Yeeesss")
			engine.runAndWait()
		elif text == "open YouTube" or text == "open youtube":
			website = "https://www.youtube.com"
			webbrowser.open_new_tab(website)
			engine.say("Sure")
			engine.runAndWait()
		elif text == "open Google" or text == "open google":
			website = "https://www.google.com"
			webbrowser.open_new_tab(website)
			engine.say("Sure")
			engine.runAndWait()
		elif text == "hi, how are you?" or text == "hi how are you" or text == "hi how are you?":
			engine.say(ans1)
			engine.runAndWait()
		elif text == "how are you?" or text == "how are you" or text == "how are you?":
			engine.say(ans1)
			engine.runAndWait()
		elif text == "open gmail" or text == "open gimail" or text == "open Gmail?":
			website = "https://mail.google.com/mail/u/0/"
			webbrowser.open_new_tab(website)
			engine.say("Sure")
			engine.runAndWait()
		elif text == "open instagram" or text == "open Instagram":
			website = "https://www.instagram.com/"
			webbrowser.open_new_tab(website)
			engine.say("Sure")
			engine.runAndWait()

			
			
			
		print("You said: {}".format(text))
	except:
		print("Sorry! I can't understand")



###UNIX ==> different way to open apps

else:
'''
r = sr.Recognizer()
how_are_you_answers = ["I'm fine thanks!", "I'm good", "I'm feeling very good today!", "Hi, I'm fine!"]
ans1 = choice(how_are_you_answers)

with sr.Microphone() as source:
	print("Say anything: ")
	audio = r.listen(source)

try:
	text = r.recognize_google(audio)
	file1 = open("./conversation.txt", "w")
	file1.write(text)
	file1.close

	if text == "ehi john" or text == "ei John" or text == "hey John" or text == "hey john":
		engine.say("Yeeesss")
		engine.runAndWait()
	elif text == "open YouTube" or text == "open youtube":
		website = "https://www.youtube.com"
		webbrowser.open_new_tab(website)
		engine.say("Sure")
		engine.runAndWait()
	elif text == "open Google" or text == "open google":
		website = "https://www.google.com"
		webbrowser.open_new_tab(website)
		engine.say("Sure")
		engine.runAndWait()
	elif text == "hi, how are you?" or text == "hi how are you" or text == "hi how are you?":
		engine.say(ans1)
		engine.runAndWait()
	elif text == "how are you?" or text == "how are you" or text == "how are you?":
		engine.say(ans1)
		engine.runAndWait()
	elif text == "open gmail" or text == "open gimail" or text == "open Gmail?":
		website = "https://mail.google.com/mail/u/0/"
		webbrowser.open_new_tab(website)
		engine.say("Sure")
		engine.runAndWait()
	elif text == "open instagram" or text == "open Instagram":
		website = "https://www.instagram.com/"
		webbrowser.open_new_tab(website)
		engine.say("Sure")
		engine.runAndWait()
	elif text == "open buzz" or text == "open dual diploma":
		website = "https://si.next.agilixbuzz.com/student"
		webbrowser.open_new_tab(website)
		engine.say("Sure")
		engine.runAndWait()
	
	elif text == "run python game" or text == "run Python game" or text == "ran python game" or text == "ran paiton game" or text == "open Python game" or text == "open python game":
		run("/Users/alexfoderaro/Coding/Git Projects/python-game/main.py")
		engine.say("Sure")
		engine.runAndWait()
	for url in search(ip, stop=20):
     	print(url)
		
	print("You said: {}".format(text))
except:
	print("Sorry! I can't understand")



