from pydantic import BaseModel

class V2Prompt(BaseModel):
    message: str
