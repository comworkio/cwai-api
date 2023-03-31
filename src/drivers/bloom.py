import torch

from transformers import AutoModelForCausalLM, AutoTokenizer
from drivers.model_driver import ModelDriver
from models.prompt import Prompt
from utils.default_values import get_max_length, get_no_repeat_ngram_size, get_num_return_sequences, get_temperature, get_top_k, get_top_p
from utils.logger import log_msg

_bloom_model_name = "bigscience/bloom"
_bloom_model = AutoModelForCausalLM.from_pretrained(_bloom_model_name)
_bloom_tokenizer = AutoTokenizer.from_pretrained(_bloom_model_name)

class BloomDriver(ModelDriver):
    def load_model(self):
        log_msg("INFO", "[bloom] loading model...")

    def generate_response(self, prompt: Prompt):
        input_ids = _bloom_tokenizer.encode(prompt.message, return_tensors="pt")
        num_return_sequences=get_num_return_sequences(prompt)
        output = _bloom_model.generate(input_ids, 
            max_length=get_max_length(prompt), 
            num_beams=5, 
            no_repeat_ngram_size=get_no_repeat_ngram_size(prompt), 
            num_return_sequences=num_return_sequences,
            do_sample=prompt.settings.do_sample,
            early_stopping=prompt.settings.early_stopping,
            top_k=get_top_k(prompt),
            top_p=get_top_p(prompt),
            temperature=get_temperature(prompt),
        )

        response = []
        for idx in range(num_return_sequences):
            response.append(_bloom_model.decode(output[idx], skip_special_tokens=prompt.settings.skip_special_tokens))
        return response
