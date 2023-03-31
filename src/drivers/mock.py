from api.prompt import Prompt
from drivers.model_driver import ModelDriver

class MockDriver(ModelDriver):
    def generate_response(self, prompt: Prompt):
        return ["Mock response for prompt = {}".format(prompt)]
