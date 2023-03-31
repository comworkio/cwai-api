from pydantic import BaseModel

class SimplePrompt(BaseModel):
    message: str
