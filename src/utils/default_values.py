import os
import json

from models.prompt import Prompt
from utils.common import is_empty, is_not_empty, is_numeric

_default_models = ['gpt2', 'nlptownsentiment', 'nltksentiment', 'textblobsentiment', 'robertaemotion', 'mock']

def get_max_length(prompt: Prompt):
    return prompt.settings.max_length if is_numeric(prompt.settings.max_length) else int(os.environ['DEFAULT_MAX_LENGTH'])

def get_num_return_sequences(prompt: Prompt):
    return prompt.settings.num_return_sequences if is_numeric(prompt.settings.num_return_sequences) else int(os.environ['DEFAULT_NUM_RETURN_SEQUENCES'])

def get_no_repeat_ngram_size(prompt: Prompt):
    return prompt.settings.no_repeat_ngram_size if is_numeric(prompt.settings.no_repeat_ngram_size) else int(os.environ['DEFAULT_NO_REPEAT_NGRAM_SIZE'])

def get_top_k(prompt: Prompt):
    return prompt.settings.top_k if is_numeric(prompt.settings.top_k) else int(os.environ['DEFAULT_TOP_K'])

def get_top_p(prompt: Prompt):
    return prompt.settings.top_p if is_not_empty(prompt.settings.top_p) else float(os.environ['DEFAULT_TOP_P'])

def get_temperature(prompt: Prompt):
    return prompt.settings.temperature if is_not_empty(prompt.settings.temperature) else float(os.environ['DEFAULT_TEMPERATURE'])

def get_all_models():
    models_json = os.getenv('ENABLED_MODELS')
    if is_empty(models_json):
        return _default_models
    try:
        return json.loads(models_json)
    except:
        return _default_models

def get_first_model():
    return get_all_models()[0]
