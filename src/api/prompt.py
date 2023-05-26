import importlib

from main import app

from fastapi import Response
from models.prompt import Prompt
from models.prompt_settings import PromptSettings
from models.simple_prompt import SimplePrompt
from utils.common import is_false
from utils.default_values import get_first_model
from utils.logger import log_msg

@app.post("/v1/prompt", status_code = 200)
def post_prompt_v1(prompt: SimplePrompt, response: Response):
    result = generate_prompt(convert_simple_to_extended(prompt), get_first_model())
    if is_false(result['status']):
        response.status_code = 400
    return result

@app.post("/v2/prompt/{model}", status_code = 200)
def post_prompt_v2(prompt: SimplePrompt, model: str, response: Response):
    result = generate_prompt(convert_simple_to_extended(prompt), model)
    if is_false(result['status']):
        response.status_code = 400
    return result

@app.post("/v3/prompt/{model}", status_code = 200)
def post_prompt_v3(prompt: Prompt, model: str, response: Response):
    result = generate_prompt(prompt, model)
    if is_false(result['status'], response: Response):
        response.status_code = 400
    return result

def convert_simple_to_extended(prompt: SimplePrompt):
    return Prompt(message=prompt.message, settings=PromptSettings())

def generate_prompt(prompt: Prompt, model: str):
    try:
        driverModule = importlib.import_module("drivers.{}".format(model.lower()))
        Driver = getattr(driverModule, "{}Driver".format(model.capitalize()))
    except ModuleNotFoundError as e:
        log_msg("WARN", "[prompt] model seems not found: {}".format(e))
        return {
            'status': 'ko',
            'response': ['model not found']
        }
    response = Driver().generate_response(prompt)
    return {
        'status': 'ok',
        'response': response
    }
