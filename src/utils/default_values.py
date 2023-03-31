import os
import json

from models.prompt import Prompt
from utils.common import is_empty, is_numeric

_default_models = ['bloom', 'gpt2', 'mock']

def get_max_length(prompt: Prompt):
    return prompt.settings.max_length if is_numeric(prompt.settings.max_length) else int(os.environ['DEFAULT_MAX_LENGTH'])

def get_num_return_sequences(prompt: Prompt):
    return prompt.settings.num_return_sequences if is_numeric(prompt.settings.num_return_sequences) else int(os.environ['DEFAULT_NUM_RETURN_SEQUENCES'])

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
