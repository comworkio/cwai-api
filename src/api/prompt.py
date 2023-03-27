from typing import Optional
from main import app
from pydantic import BaseModel
from utils.gpt2 import generate_response, _default_max_length, _default_num_return_sequences

class Prompt(BaseModel):
    message: str
    max_length: Optional[int] = _default_max_length
    num_return_sequences: Optional[int] = _default_num_return_sequences

@app.post("/v1/prompt")
@app.post("/v2/prompt/gpt2")
def post_gpt2_prompt(prompt: Prompt):
    response = generate_response(prompt.message, prompt.max_length, prompt.num_return_sequences)
    return {
        'status': 'ok',
        'response': response
    }
