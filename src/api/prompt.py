from main import app
from pydantic import BaseModel
from utils.gpt2 import generate_response

class Prompt(BaseModel):
    prompt: str
    max_length: int | None
    num_return_sequences: int | None

@app.post("/v1/prompt")
def post_prompt(prompt: Prompt):
    response = generate_response(prompt.prompt, )
    return {
        'status': 'ok',
        'response': response
    }
