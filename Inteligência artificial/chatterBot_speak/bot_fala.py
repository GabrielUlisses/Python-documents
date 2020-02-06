# -*- coding: utf-8 -*-
import chatterbot
from chatterbot.trainers import *
import speech_recognition as sr
import pyttsx3

def Speak(text):
    speak.say(text)
    speak.runAndWait()
    
bot = chatterbot.ChatBot('Mirtheyl',storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3')
speak = pyttsx3.init('sapi5')

conv = ['ola','oi','oi','ola','bom dia','bom dia','boa tarde','boa tarde','boa noite','boa noite','tudo bom?','tudo bem','tudo bom','tudo e você','tudo bom?','mais ou menos na verdade, e você?']
xingar = ['você é um idiota','...']

trainer= ListTrainer(bot)
trainer.train(conv)
trainer.train(xingar)

r = sr.Recognizer()
print('construct')
with sr.Microphone() as micro:
    r.adjust_for_ambient_noise(s)
    print('Say something:')
    
    while True:
        try:    
            audio = r.listen(s)
            speech = r.recognize_google(audio)
            response = bot.get_response(speech)
            print('You:', speech)
            print('bot:', response)
            Speak(response)
        except:
            print('erro ao tentar responder...')
