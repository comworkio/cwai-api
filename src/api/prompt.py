import importlib

from typing import Optional
from main import app

from models.prompt import Prompt
from utils.default_values import get_first_model

@app.post("/v1/prompt")
def post_prompt_v1(prompt: Prompt):
    return generate_prompt(prompt, get_first_model())

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
