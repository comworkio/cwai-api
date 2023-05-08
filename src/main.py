import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.common import is_true
from utils.logger import log_msg

def load_apis():
    from api.health import get_health
    from api.manifest import get_manifest
    from api.models import get_models
    from api.prompt import post_prompt_v1, post_prompt_v2, post_prompt_v3

version = os.environ['VERSION']
log_msg("INFO", "[main] the application is starting with version = {}".format(version))
app = FastAPI(title="cwai-api", version=version, docs_url="/")

if os.getenv('APP_ENV') == 'local' or is_true(os.getenv('ENABLE_CORS_ALLOW_ALL')):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

load_apis()
