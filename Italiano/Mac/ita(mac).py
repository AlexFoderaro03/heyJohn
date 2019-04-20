import speech_recognition as sr
import webbrowser
import os
from termcolor import colored
import keyboard
import subprocess
from googlesearch import search
import random
import sys
import requests
from random import choice
import pyttsx3


engine = pyttsx3.init()
engine.setProperty("rate", 160)
engine.setProperty('voice', 'Luca')
def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())
file1 = open("yourname.txt", "r")
name = file1.readline()
file2 = open("music.txt", "r")
songPref = file2.readline()


print()
print()
print()

def main():
	while True:
		b = sr.Recognizer()
		with sr.Microphone() as source:
			audio = b.listen(source)
		try:
			text = b.recognize_google(audio, language="it-IT")
			if text == "Ehi John" or text == "Ei John" or text == "Hei John" or text == "Hei john" or text == "Okay John" or text == "Ok John" or text == "OK John":
				engine.say("Dimmi ..." )
				engine.runAndWait()
				john()
			elif text == "Esci" or text == "stop" or text == "Fermati" or text == "Stop" or text == "esci":
				quit()
			else:
				main()
		except:
			icantUndersatand = colored("Non ho capito", "red")

def john():
	while True:
		r = sr.Recognizer()
		how_are_you_answers = ["Sto bene grazie", "Sto bene", "Sto molto bene oggi", "Bene, grazie"]
		hi_q = ["Ciao!", "Hey ciao", "Eilà"]
		jokes = ["Che cosa hanno in comune un televisore e una formica? Le antenne!", "Qual è la città preferita dai ragni? Mosca!", "Qual è la pianta più puzzolente? Quella dei piedi!", "Che cos'è una zebra? Un cavallo evaso dal carcere!", "Sapete perché il pomodoro non riesce a dormire? Perché l’insalata… russa!", "Cosa fa un carabiniere in aeroporto? Offre noccioline al Jumbo!", "Qual è il cane più cattivo? La canaglia", "Il miglior cane da guardia è lo 00 Setter.", "Qual è il colmo per un macellaio quando cambia discorso? Tagliare la testa al toro", "Come si dice uno scontro tra due carrelli? Scontrino!", "Cosa fa il dente del giudizio? Giudica i molari! ", "Quale sistema operativo non possono usare i ciechi? Windows Vista.", "Un poliziotto va da una gang di computer: 'vi arresto il sistema'. ", "Se sentite delle sirene avvicinarsi non vi preoccupate. Ho appena arrestato il PC! "]
		ceninii = ["Hai avuto una conoscienza approfondita del capitolo. Spesso sei entrato anche nei particolari. Hai riscontrato un po' di difficoltà e incertezza in letteratura. Possiamo dire che è stata un interrogazione discreta. Ti do 7 +", "Questa verifica è andata abbastanza bene. Qualche erore di grammatica e di lessico. Tutto sommato hai fatto una buona verifica. Ti do 6 e mezzo, anzi no. Ti do 6 +"]
		jc = choice(ceninii)
		jk = choice(jokes)
		ans1 = choice(how_are_you_answers)
		ans2 = choice(hi_q)

		with sr.Microphone() as source:
			print(colored("Di qualcosa: ", "blue"))
			audio = r.listen(source)

		try:
			text = r.recognize_google(audio, language="it-IT")

			if text == "ciao" or text == "Ciao" or text == "Ciao Jon" or text == "Ciao John":
				engine.say(ans2)
				engine.runAndWait()
				if text == "Sto bene grazie" or text == "Bene grazie" or text == "Bene":
					engine.say("Sono felice che tu stia bene!")
					engine.runAndWait()
				elif text == "Bene e tu" or text == "Sto bene e tu" or text == "Bene grazie e tu" or text == "Sto bene e te":
					engine.say("Anche io!")
			elif text == "Come stai" or text == "Come va" or text == "Ciao come stai" or text == "Ciao John come stai" or text == "come va":
				engine.say("Sto benissimo!")
				engine.runAndWait()
			elif text == "Ciao Cenini" or text == "Ciao cenini" or text == "Cenini" or text == "cenini" or text == "Ciao Daniele" or text == "ciao Daniele" :
				engine.say(jc)
				engine.runAndWait()
			elif text == "Apri YouTube" or text == "Aprimi YouTube" or text == "Puoi aprire YouTube" or text == "Puoi aprirmi youtube" or text == "Puoi aprirmi YouTube":
				engine.say("Certo")
				engine.runAndWait()
				website = "https://www.youtube.com"
				webbrowser.open_new_tab(website)
			elif text == "Apri Google" or text == "Aprimi google" or text == "Puoi aprire Google" or text == "Puoi aprirmi google" or text == "Puoi aprirmi google":
				engine.say("Certo", name)
				engine.runAndWait()
				website = "https://www.google.com"
				webbrowser.open_new_tab(website)
			elif text == "Apri gmail" or text == "Aprimi Gmail" or text == "Puoi aprire gmail" or text == "Puoi aprirmi Gmail" or text == "Puoi aprire Gmail":
				engine.say("Certo")
				engine.runAndWait()
				website = "https://mail.google.com/mail/u/0/"
				webbrowser.open_new_tab(website)
			elif text == "Apri Instagram" or text == "Aprimi Instagram" or text == "Puoi aprire Instagram" or text == "Puoi aprirmi Instagram" or text == "Puoi aprirmi Instagram":
				engine.say("Certo")
				engine.runAndWait()
				website = "https://www.instagram.com/"
				webbrowser.open_new_tab(website)
			elif text == "Apri WhatsApp" or text == "Aprimi WhatsApp" or text == "Puoi aprire WhatsApp" or text == "Puoi aprirmi WhatsApp" or text == "Puoi aprirmi WhatsApp":
				engine.say("Certo")
				engine.runAndWait()
				website = "https://web.whatsapp.com/"
				webbrowser.open_new_tab(website)
			elif text == "Apri il dizionario di latino" or text == "Puoi aprirmi il dizionario di latino" or text == "Aprimi il dizionario di latino" or text == "Puoi aprirmi il dizionario di latino":
				engine.say("Certo")
				engine.runAndWait()
				website = "https://www.dizionario-latino.com/"
				webbrowser.open_new_tab(website)
			elif text == "Apri GitHub" or text == "Puoi aprirmi GitHub" or text == "Aprimi github" or text == "Puoi aprirmi github":
				engine.say("Certo")
				engine.runAndWait()
				website = "https://github.com/"
				webbrowser.open_new_tab(website)
			elif text == "Apri Google Drive" or text == "Apri drive" or text == "Puoi aprire Google Drive" or text == "apri Google Drive":
				engine.say("Certo")
				engine.runAndWait()
				website = "https://drive.google.com/drive/u/0/my-drive"
				webbrowser.open_new_tab(website)
			elif text == "Grazie" or text == "Grazie mille" or text == "grazie":
				engine.say("Sono felice di accontentarti", name)
				engine.runAndWait()
			elif text == "Come ti chiami" or text == "Qual'è il tuo nome" :
				engine.say("Mi chiamo John. Sono stato programmato da Alex Foderaro. Seguilo su Instagram")
				engine.runAndWait()
			elif text == "Come mi chiamo" or text == "Qual'è il mio nome" :
				engine.say(name)
				engine.runAndWait()
			elif text == "Impostami un'allarme" or text == "Imposta una sveglia" or text == "Puoi impostarmi una sveglia" or text == "Mi imposti una sveglia":
				engine.say("Sto accendendo l'orologio", name)
				engine.runAndWait()
				os.system('python3 alarm.py')
			elif text == "Lancia una moneta" or text == "lancia una moneta":
				flip = ["testa", "croce"]
				ans3 = choice(flip)
				engine.say(ans3)
				engine.runAndWait()
				print(ans3)
				print()
				print()
				print()
			elif text == "esplodi" or text == "Esplodi" or text == "autodistruzione":
				engine.say("bi bi bi bi bip. Bouuuummm. Sono esploduto ")
				engine.runAndWait()

			elif text == "Riproduci della musica" or text == "riproduci della musica" or text == "Riproduci un po' di musica" or text == "riproduci un po' di musica" or text == "musica" or text == "Musica" or text == "metti un po' di musica" or text == "Metti un po' di musica":
				if songPref == "Spotify":
					engine.say("Certo! Sto aprendo Spotify")
					engine.runAndWait()
					os.system("open /Applications/Spotify.app")
				else:
					engine.say("Certo! Sto aprendo iTunes")
					engine.runAndWait()
					os.system("open /Applications/iTunes.app")

				elif text == "Apri Spotify" or text == "apri Spotify":
					engine.say("Certo! Sto aprendo Spotify")
					engine.runAndWait()
					os.system("open /Applications/Spotify.app")

				elif text == "Apri iTunes" or text == "apri iTunes":
					engine.say("Certo! Sto aprendo iTunes")
					engine.runAndWait()
					os.system("open /Applications/iTunes.app")



			elif text == "Ciao Teresa" or text == "ciao Teresa" or text == "ciao teresa":
				engine.say("Ciao Daniele, la vuoi una caramella?. C'è Cialluca?")
				engine.runAndWait()
			elif text == "Quanti anni hai?" or text == "Quanti anni hai":
				engine.say("L'età è un indicatore difficile da contare per un'intelligenza artificiale. Potrei contare le righe del mio codice ma una volta finito, sarò già cresciuto.")
				engine.runAndWait()
			elif text == "Raccontami una barzelletta" or text == "Dimmi una barzelletta" or text == "barzelletta" or text == "Hey dimmi una barzelletta":
				engine.say(jk)
				engine.runAndWait()
			elif text == "Esci" or text == "esci" or text == "Stop" or text == "Fermati" or text == "stop":
				quit()
			print()
			print()
			print()
			print(colored("Hai detto : {}".format(text), "yellow"))
			print()
			print()
			print()
		except:
			if text == "Esci" or text == "esci" or text == "Stop" or text == "Fermati" or text == "stop":
				quit()
			icantUndersatand = colored("Scusa, non ho capito", "red")
			print(icantUndersatand, name)

main()