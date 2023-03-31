import torch

from transformers import AutoModelForCausalLM, AutoTokenizer
from drivers.model_driver import ModelDriver
from models.prompt import Prompt
from utils.logger import log_msg
from utils.transformers_utils import get_response

_bloom_model_name = "bigscience/bloom"
_bloom_model = AutoModelForCausalLM.from_pretrained(_bloom_model_name)
_bloom_tokenizer = AutoTokenizer.from_pretrained(_bloom_model_name)

class BloomDriver(ModelDriver):
    def load_model(self):
        log_msg("INFO", "[bloom] loading model...")

    def generate_response(self, prompt: Prompt):
        return get_response(prompt, _bloom_tokenizer, _bloom_model)
