import os
import importlib

from fastapi import FastAPI
from utils.default_values import get_all_models
from utils.logger import log_msg

def load_apis():
    from api.health import get_health
    from api.manifest import get_manifest
    from api.models import get_models
    from api.prompt import post_prompt_v1, post_prompt_v2, post_prompt_v3

def load_models():
    models = get_all_models()
    log_msg("INFO", "Loading models : {}".format(models))
    for model in models:
        driverModule = importlib.import_module("drivers.{}".format(model.lower()))
        Driver = getattr(driverModule, "{}Driver".format(model.capitalize()))
        Driver().load_model()

version = os.environ['VERSION']
log_msg("INFO", "[main] the application is starting with version = {}".format(version))
app = FastAPI(title="cwai-api", version=version, docs_url="/")
load_apis()
load_models()
