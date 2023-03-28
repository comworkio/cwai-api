from main import app
from utils.default_values import _models

@app.get("/v1/models")
def get_models():
    return {
        'status': 'ok',
        'models': _models
    }
