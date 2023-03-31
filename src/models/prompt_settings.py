import os

from pydantic import BaseModel
from typing import Optional

class PromptSettings(BaseModel):
    max_length: Optional[int] = int(os.environ['DEFAULT_MAX_LENGTH'])
    num_return_sequences: Optional[int] = int(os.environ['DEFAULT_NUM_RETURN_SEQUENCES'])
