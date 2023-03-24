from main import app

@app.get("/v1/health")
def get_health():
    return {
        'status': 'ok',
        'alive': True
    }
