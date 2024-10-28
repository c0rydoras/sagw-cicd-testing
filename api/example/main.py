from __future__ import annotations

from fastapi import FastAPI

app = FastAPI(root_path="/api/v1")


@app.get("/hello")
def hello():
    """Hello World."""
    return {"message": "Hello World!"}
