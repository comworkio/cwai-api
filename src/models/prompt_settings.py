import os

from pydantic import BaseModel
from typing import Optional

class PromptSettings(BaseModel):
    max_length: Optional[int] = int(os.environ['DEFAULT_MAX_LENGTH'])
    num_return_sequences: Optional[int] = int(os.environ['DEFAULT_NUM_RETURN_SEQUENCES'])
    no_repeat_ngram_size: Optional[int] = int(os.environ['DEFAULT_NO_REPEAT_NGRAM_SIZE'])
    early_stopping: Optional[bool] = True
    do_sample: Optional[bool] = True
    skip_special_tokens: Optional[bool] = True
    top_k: Optional[int] = int(os.environ['DEFAULT_TOP_K'])
    top_p: Optional[float] = float(os.environ['DEFAULT_TOP_P'])
    temperature: Optional[float] = float(os.environ['DEFAULT_TEMPERATURE'])
