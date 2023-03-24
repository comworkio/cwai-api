from main import app
from pydantic import BaseModel
from utils.gpt2 import generate_response, _default_max_length, _default_num_return_sequences

class Prompt(BaseModel):
    message: str
    max_length: int | _default_max_length
    num_return_sequences: int | _default_num_return_sequences

@app.post("/v1/prompt")
def post_prompt(prompt: Prompt):
    response = generate_response(prompt.message, prompt.max_length, prompt.num_return_sequences)
    return {
        'status': 'ok',
        'response': response
    }
