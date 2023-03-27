from main import app

@app.get("/v1/models")
def get_models():
    return {
        'status': 'ok',
        'models': ['gpt2']
    }
