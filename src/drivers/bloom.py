import torch

from transformers import AutoModelForCausalLM, AutoTokenizer
from drivers.model_driver import ModelDriver
from models.prompt import Prompt
from utils.default_values import get_max_length

_bloom_model_name = "turing-mt/bloom-100-english"
_bloom_model = AutoModelForCausalLM.from_pretrained(_bloom_model_name)
_bloom_tokenizer = AutoTokenizer.from_pretrained(_bloom_model_name)

class BloomDriver(ModelDriver):
    def generate_response(self, prompt: Prompt):
        input_ids = _bloom_tokenizer.encode(prompt.message, return_tensors="pt")
        output = _bloom_model.generate(input_ids, 
            max_length=get_max_length(prompt), 
            num_beams=5, 
            no_repeat_ngram_size=2, 
            early_stopping=True
        )

        return [_bloom_tokenizer.decode(output[0], skip_special_tokens=True)]
