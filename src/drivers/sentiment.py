from drivers.model_driver import ModelDriver
from models.prompt import Prompt
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
from utils.logger import log_msg

_sentiment_model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
_sentiment_model = AutoModelForSequenceClassification.from_pretrained(_sentiment_model_name)
_sentiment_tokenizer = AutoTokenizer.from_pretrained(_sentiment_model_name)

emotion_mapping = {
    1: 'Anger',
    2: 'Dislike',
    3: 'Neutral',
    4: 'Like',
    5: 'Love'
}

class SentimentDriver(ModelDriver):
    def load_model(self):
        log_msg("INFO", "[sentiment] loading model...")

    def generate_response(self, prompt: Prompt):
        inputs = _sentiment_tokenizer(prompt.message, return_tensors="pt")
        outputs = _sentiment_model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
        predicted_class = torch.argmax(probs).item() + 1
        predicted_emotion = emotion_mapping[predicted_class]
        return ["The predicted emotion is: {}".format(predicted_emotion)]