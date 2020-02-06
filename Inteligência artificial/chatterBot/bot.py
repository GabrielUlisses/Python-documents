# -*- coding: utf-8 -*-
import chatterbot
from chatterbot.trainers import *

bot = chatterbot.ChatBot(
    'Mirtheyl',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters = [
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ],
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
    database_uri='sqlite:///database.sqlite3'
    )

ctrainer = ChatterBotCorpusTrainer(bot)
ctrainer.train(
    "chatterbot.corpus.portuguese.compliment",
    "chatterbot.corpus.portuguese.conversations",
    "chatterbot.corpus.portuguese.greetings",
    "chatterbot.corpus.portuguese.linguistic_knowledge",
    "chatterbot.corpus.portuguese.proverbs",
    "chatterbot.corpus.portuguese.suggestions",
    "chatterbot.corpus.portuguese.trivia",
    "chatterbot.corpus.portuguese.unilab",
    "chatterbot.corpus.portuguese",
    )

while True:
    try:    
        quest = input('Você: ')
        response = bot.get_response(quest)
        if float(response.confidence) > 0.5:
            print('Bot: ',response)
        else:
            print('Bot: ',response,'(inseguro %s)'%response.confidence)
    except(KeyboardInterrupt, EOFError, SystemExit):
        print('erro ao tentar responder...')
        break
