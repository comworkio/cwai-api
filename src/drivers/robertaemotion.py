# Choosing a pretrained model from hugging face because it's more
# rewarding in terms of accuracy than a basic model that i would train from scratch
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer
import numpy as np
from scipy.special import softmax
import csv
import urllib.request
from drivers.model_driver import ModelDriver
from models.prompt import Prompt
from utils.logger import log_msg


task = 'emotion'
MODEL = f"cardiffnlp/twitter-roberta-base-{task}"

tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)
# label mapping
labels = ["anger", "joy", "optimism", "sadness"]


# Saving the model and tokenizer so that we don't have to load them each time we run the container
model.save_pretrained(MODEL)
tokenizer.save_pretrained(MODEL)


class RobertaemotionDriver(ModelDriver):
    def load_model(self):
        log_msg("INFO", "[RobertaEmotion] loading model...")

    def generate_response(self, prompt: Prompt):
        text = prompt.message
        encoded_input = tokenizer(text, return_tensors='pt')
        output = model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        msg = ""
        for i in range(scores.shape[0]):
            l = labels[ranking[i]]
            s = scores[ranking[i]]
            msg += str(l) + " "+str(np.round(float(s), 4))+"; "
            print(f"{i+1}) {l} {np.round(float(s), 4)}")
        return {"response": ["The predicted emotions are: {}".format(msg)]}
