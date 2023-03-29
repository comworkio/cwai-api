import os

from drivers.model_driver import ModelDriver

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

_chatbot = ChatBot("chatterbot-cwai-{}".format(os.environ['VERSION']))
_trainer = ChatterBotCorpusTrainer(_chatbot)
_trainer.train('chatterbot.corpus.english')

class ChatterbotDriver(ModelDriver):
    def generate_response(self, prompt, _max_length, _num_return_sequences):
        return chatbot.get_response(prompt)
