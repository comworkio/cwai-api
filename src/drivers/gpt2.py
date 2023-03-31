from models.prompt import Prompt
from drivers.model_driver import ModelDriver

from transformers import GPT2LMHeadModel, GPT2Tokenizer
from utils.logger import log_msg
from utils.transformers_utils import get_response

_gpt2_model_name = 'gpt2'
_gpt2_tokenizer = GPT2Tokenizer.from_pretrained(_gpt2_model_name)
_gpt2_model = GPT2LMHeadModel.from_pretrained(_gpt2_model_name)

class Gpt2Driver(ModelDriver):
    def load_model(self):
        log_msg("INFO", "[gpt2] loading model...")

    def generate_response(self, prompt: Prompt):
        return get_response(prompt, _gpt2_tokenizer, _gpt2_model)
