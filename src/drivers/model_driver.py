from abc import ABC, abstractmethod

from models.prompt import Prompt

class ModelDriver(ABC):
    @abstractmethod
    def generate_response(self, prompt: Prompt):
        pass
