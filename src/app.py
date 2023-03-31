from multiprocessing import Process
from utils.models_loader import load_models
import uvicorn
import os

async_process = Process( 
    target=load_models,
    daemon=True
)
async_process.start()

if __name__ == "__main__":
    uvicorn.run("main:app", host=os.environ['LISTEN_ADDR'], port=int(os.environ['LISTEN_PORT']), reload=True)
