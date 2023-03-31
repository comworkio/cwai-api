import importlib

from typing import Optional
from main import app
from pydantic import BaseModel

from utils.default_values import _models, _default_max_length, _default_num_return_sequences

class PromptSettings(BaseModel):
    max_length: Optional[int] = _default_max_length
    num_return_sequences: Optional[int] = _default_num_return_sequences

class Prompt(BaseModel):
    message: str
    settings: PromptSettings

@app.post("/v1/prompt")
def post_prompt_v1(prompt: Prompt):
    return generate_prompt(prompt, _models[0])

@app.post("/v2/prompt/{model}")
def post_prompt_v2(prompt: Prompt, model: str):
    return generate_prompt(prompt, model)

def generate_prompt(prompt: Prompt, model: str):
    driverModule = importlib.import_module("drivers.{}".format(model.lower()))
    Driver = getattr(driverModule, "{}Driver".format(model.capitalize()))
    response = Driver().generate_response(prompt)
    return {
        'status': 'ok',
        'response': response
    }
