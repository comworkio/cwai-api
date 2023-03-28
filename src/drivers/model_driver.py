from abc import ABC, abstractmethod

class ModelDriver(ABC):
    @abstractmethod
    def generate_response(self, prompt, _max_length, _num_return_sequences):
        pass
