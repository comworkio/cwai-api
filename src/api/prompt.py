import importlib

from main import app

from models.prompt import Prompt
from models.prompt_settings import PromptSettings
from models.simple_prompt import SimplePrompt
from utils.common import is_true
from utils.default_values import get_first_model
from utils.logger import log_msg

@app.post("/v1/prompt")
def post_prompt_v1(prompt: SimplePrompt):
    result = generate_prompt(convert_simple_to_extended(prompt), get_first_model())
    return result, 200 if is_true(result['status']) else 400

@app.post("/v2/prompt/{model}")
def post_prompt_v2(prompt: SimplePrompt, model: str):
    result = generate_prompt(convert_simple_to_extended(prompt), model)
    return result, 200 if is_true(result['status']) else 400

@app.post("/v3/prompt/{model}")
def post_prompt_v3(prompt: Prompt, model: str):
    result = generate_prompt(prompt, model)
    return result, 200 if is_true(result['status']) else 400

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
