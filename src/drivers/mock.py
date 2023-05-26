from models.prompt import Prompt
from drivers.model_driver import ModelDriver
from utils.logger import log_msg

class MockDriver(ModelDriver):
    def load_model(self):
        log_msg("INFO", "[mock] loading model...")

    def generate_response(self, prompt: Prompt):
        return { "response": ["Mock response for prompt = {}".format(prompt)] }
