import os

_default_max_length = int(os.environ['DEFAULT_MAX_LENGTH'])
_default_num_return_sequences = int(os.environ['DEFAULT_NUM_RETURN_SEQUENCES'])
_models = ['gpt2', 'chatterbot', 'mock']
