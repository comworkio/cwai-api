import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

from utils.logger import log_msg
from drivers.model_driver import ModelDriver
from models.prompt import Prompt

nltk.download('vader_lexicon')
_sia = SentimentIntensityAnalyzer()

class NltksentimentDriver(ModelDriver):
    def load_model(self):
        log_msg("INFO", "[Nltksentiment] loading model...")

    def generate_response(self, prompt: Prompt):
        scores = _sia.polarity_scores(prompt.message)
        
        if scores['compound'] >= 0.05:
            sentiment = 'postive'
        elif scores['compound'] <= -0.05:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        
        return { "response": ["The predicted sentiment is: {}, score: {}".format(sentiment, scores['compound'])], "score": scores['compound'] }
