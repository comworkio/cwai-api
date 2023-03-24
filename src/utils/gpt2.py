from transformers import GPT2LMHeadModel, GPT2Tokenizer

_model_name = 'gpt2'
_tokenizer = GPT2Tokenizer.from_pretrained(_model_name)
_model = GPT2LMHeadModel.from_pretrained(_model_name)

def generate_response(prompt, num_return_sequences=1, max_length=50):
    input_ids = _tokenizer.encode(prompt, return_tensors='pt')
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
