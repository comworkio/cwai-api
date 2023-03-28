from drivers.model_driver import ModelDriver

class MockDriver(ModelDriver):
    def generate_response(self, prompt, _max_length, _num_return_sequences):
        return ["Mock response for prompt = {}, _max_length = {}, _num_return_sequences = {}".format(prompt, _max_length, _num_return_sequences)]
