import os

from models.prompt import Prompt
from utils.common import is_numeric

_models = ['gpt2', 'bloom', 'mock']

def get_max_length(prompt: Prompt):
    return prompt.settings.max_length if is_numeric(prompt.settings.max_length) else int(os.environ['DEFAULT_MAX_LENGTH'])

def get_num_return_sequences(prompt: Prompt):
    return prompt.settings.num_return_sequences if is_numeric(prompt.settings.num_return_sequences) else int(os.environ['DEFAULT_NUM_RETURN_SEQUENCES'])

def get_all_models():
    return _models

def get_first_model():
    return _models[0]
