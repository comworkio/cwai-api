
from pydantic import BaseModel
from models.prompt_settings import PromptSettings

class Prompt(BaseModel):
    message: str
    settings: PromptSettings
