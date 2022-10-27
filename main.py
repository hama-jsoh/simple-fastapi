import uvicorn
from fastapi import FastAPI
from routes import test


def create_app():
    app = FastAPI()
    app.include_router(test.router, tags=["test"], prefix="/test")
    return app

app = create_app()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8890, reload=True)
