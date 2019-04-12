import speech_recognition as sr
import webbrowser
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
hi_q = ["Hi!", "Hello", "hi", "Hi there!", "Hi there", "Hi how are you?", "Hi what's up?"]

ans1 = choice(how_are_you_answers)
ans2 = choice(hi_q)

with sr.Microphone() as source:
	print("Say anything: ")
	audio = r.listen(source)

try:
	text = r.recognize_google(audio)

	if text == "ehi john" or text == "ei John" or text == "hey John" or text == "hey john":
		engine.say("Yeeesss")
		engine.runAndWait()
	elif text == "hi" or text == "hai":
		engine.say(ans2)
		engine.runAndWait()
		if text == "i'm fine" or text == "i'm fine thanks" or text == "I'm fine" or text == "i'm fine" or text == "i'm good thanks":
			engine.say("I'm happy you are fine!")
			engine.runAndWait()
		elif text == "i'm fine and you" or text == "fine and you" or text == "i'm good and you" or text == "i'm fine and you":
			engine.say("I'm fine!")
	elif text == "how are you" or text == "how are you feeling" or text == "hi how are you" or text == "hello how you are you feeling":
		engine.say("I'm fine thanks")
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
	elif text == "open buzz" or text == "open dual diploma" or text == "duel diploma":
		website = "https://si.next.agilixbuzz.com/student"
		webbrowser.open_new_tab(website)
		engine.say("Sure")
		engine.runAndWait()
	elif text == "open whatsapp" or text == "open what's app" or text == "open whats app" or text == "open WhatsApp":
		website = "https://web.whatsapp.com/"
		webbrowser.open_new_tab(website)
		engine.say("Sure")
		engine.runAndWait()
	elif text == "open latin dictionary" or text == "open Latin's dictionary" or text == "open Latin dictionary" or text == "open late dictionary" or text == "open late in dictionary"
		website = "https://www.dizionario-latino.com/"
		webbrowser.open_new_tab(website)
		engine.say("Sure")
		engine.runAndWait()
	'''
	elif text == "run python game" or text == "run Python game" or text == "ran python game" or text == "ran paiton game" or text == "open Python game" or text == "open python game":
		run("/Users/alexfoderaro/Coding/Git Projects/python-game/main.py")
		engine.say("Sure")
		engine.runAndWait()
	'''
	print("You said: {}".format(text))
except:
	print("Sorry! I can't understand")


