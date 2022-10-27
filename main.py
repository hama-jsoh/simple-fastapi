import uvicorn
import argparse
from fastapi import FastAPI
from routes import test


def set_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("-h", "--host", type=str, default="0.0.0.0", help="Bind socket to this host. [default: 0.0.0.0]")
    parser.add_argument("-p", "--port", type=int, default="8000", help="Bind socket to this host. [default: 8000]")
    args = parser.parse_args()
    return args

def create_app():
    app = FastAPI()
    app.include_router(test.router, tags=["test"], prefix="/test")
    return app

ARGS = set_argument()
HOST = ARGS.host
PORT = ARGS.port

app = create_app()


if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
