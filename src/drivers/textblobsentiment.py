from textblob import TextBlob

from utils.logger import log_msg
from drivers.model_driver import ModelDriver
from models.prompt import Prompt

class TextblobsentimentDriver(ModelDriver):
    def load_model(self):
        log_msg("INFO", "[Textblobsentiment] loading model...")

    def generate_response(self, prompt: Prompt):
        blob = TextBlob(prompt.message)
        polarity = blob.sentiment.polarity
        
        if polarity > 0:
            sentiment = 'Postive'
        elif polarity < 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
        
        return { "response": ["The predicted sentiment is: {}".format(sentiment)], "score": polarity }
