from main import app
from utils.default_values import get_all_models

@app.get("/v1/models")
def get_models():
    return {
        'status': 'ok',
        'models': get_all_models()
    }
