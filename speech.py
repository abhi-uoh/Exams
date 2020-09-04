
# Create a reusable library that can convert a paragraph of spoken english to written english. For example, "two dollars" should be converted to $2. Abbreviations spoken as "C M" or "Triple A" should be written as "CM" and "AAA" respectively.
# Push your code to a public github/gitlab/bitbucket repo and submit the link here.

import pyttsx3
import speech_recognition as sr

def takeInput():
	r = sr.Recognizer()
	dictionary= {
		"single": 1,
		"double": 2,
		"triple": 3,
		"quadruple": 4,
		"quintuple": 5,
		"sextuple": 6,
		"septuple": 7,
		"octuple": 8,
		"nonuple": 9,
		"decuple": 10
	}
	with sr.Microphone() as source:
		print("Listening")
		r.pause_threshold = 1
		audio = r.listen(source)
	try:
		print("recognizing...")
		query = str(r.recognize_google(audio, language='en-in'))
		print(query)
		word = query.split(" ")
		if word[0] in dictionary.keys():
			text = ''
			for w in word[1:]:
				text+=w
			print((dictionary[word[0]]*text).upper())
	except Exception as e:
		print("Speak again")


if _name_ == '_main_':
	takeInput()
