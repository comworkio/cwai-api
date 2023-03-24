from fastapi import FastAPI
from utils.logger import log_msg
import os

def load_apis():
    from api.health import get_health
    from api.manifest import get_manifest
    from api.prompt import post_prompt

log_msg("INFO", "[main] the application is starting with version = {}".format(os.environ['VERSION']))
app = FastAPI(docs_url="/")
load_apis()
