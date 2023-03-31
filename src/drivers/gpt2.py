from models.prompt import Prompt
from drivers.model_driver import ModelDriver

from transformers import GPT2LMHeadModel, GPT2Tokenizer
from utils.default_values import get_max_length, get_no_repeat_ngram_size, get_num_return_sequences, get_temperature, get_top_k, get_top_p
from utils.logger import log_msg

_gpt2_model_name = 'gpt2'
_gpt2_tokenizer = GPT2Tokenizer.from_pretrained(_gpt2_model_name)
_gpt2_model = GPT2LMHeadModel.from_pretrained(_gpt2_model_name)

class Gpt2Driver(ModelDriver):
    def load_model(self):
        log_msg("INFO", "[gpt2] loading model...")

    def generate_response(self, prompt: Prompt):
        input_ids = _gpt2_tokenizer.encode(prompt.message, return_tensors='pt')
        num_return_sequences = get_num_return_sequences(prompt)
        output = _gpt2_model.generate(
            input_ids,
            max_length=get_max_length(prompt),
            num_return_sequences=num_return_sequences,
            no_repeat_ngram_size=get_no_repeat_ngram_size(prompt),
            do_sample=prompt.settings.do_sample,
            early_stopping=prompt.settings.early_stopping,
            top_k=get_top_k(prompt),
            top_p=get_top_p(prompt),
            temperature=get_temperature(prompt),
        )

        response = []
        for idx in range(num_return_sequences):
            response.append(_gpt2_tokenizer.decode(output[idx], skip_special_tokens=prompt.settings.skip_special_tokens))
        return response
