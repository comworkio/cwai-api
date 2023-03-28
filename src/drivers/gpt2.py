import os
from drivers.model_driver import ModelDriver

from transformers import GPT2LMHeadModel, GPT2Tokenizer
from utils.common import is_numeric
from utils.default_values import _default_max_length, _default_num_return_sequences

_model_name = 'gpt2'
_tokenizer = GPT2Tokenizer.from_pretrained(_model_name)
_model = GPT2LMHeadModel.from_pretrained(_model_name)

class Gpt2Driver(ModelDriver):
    def generate_response(self, prompt, _max_length, _num_return_sequences):
        input_ids = _tokenizer.encode(prompt, return_tensors='pt')
        max_length = _max_length if is_numeric(_max_length) else _default_max_length
        num_return_sequences = _num_return_sequences if is_numeric(_num_return_sequences) else _default_num_return_sequences

        output = _model.generate(
            input_ids,
            max_length=max_length,
            num_return_sequences=num_return_sequences,
            no_repeat_ngram_size=2,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.8,
        )

        response = []
        for idx in range(num_return_sequences):
            response.append(_tokenizer.decode(output[idx], skip_special_tokens=True))
        return response
