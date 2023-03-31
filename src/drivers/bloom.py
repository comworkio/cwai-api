import torch

from transformers import AutoModelForCausalLM, AutoTokenizer
from drivers.model_driver import ModelDriver
from models.prompt import Prompt
from utils.default_values import get_max_length, get_num_return_sequences
from utils.logger import log_msg

_bloom_model_name = "bigscience/bloom"
_bloom_model = AutoModelForCausalLM.from_pretrained(_bloom_model_name)
_bloom_tokenizer = AutoTokenizer.from_pretrained(_bloom_model_name)

class BloomDriver(ModelDriver):
    def load_model(self):
        log_msg("INFO", "[bloom] loading model...")

    def generate_response(self, prompt: Prompt):
        input_ids = _bloom_tokenizer.encode(prompt.message, return_tensors="pt")
        output = _bloom_model.generate(input_ids, 
            max_length=get_max_length(prompt), 
            num_beams=5, 
            no_repeat_ngram_size=2, 
            num_return_sequences=get_num_return_sequences(prompt),
            early_stopping=True
        )

        return [_bloom_tokenizer.decode(output[0], skip_special_tokens=True)]
