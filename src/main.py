from fastapi import FastAPI
from utils.logger import log_msg
import os

def load_apis():
    from api.health import get_health
    from api.manifest import get_manifest
    from api.models import get_models
    from api.prompt import post_gpt2_prompt

version = os.environ['VERSION']
log_msg("INFO", "[main] the application is starting with version = {}".format(version))
app = FastAPI(title="cwai-api", version=version, docs_url="/")
load_apis()
