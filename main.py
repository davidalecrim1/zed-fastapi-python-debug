import logging
import os

from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

ENV_KEYS = [
    "MY_VARIABLE",
]


@app.on_event("startup")
def print_env():
    for key in ENV_KEYS:
        logger.info(f"{key}={os.environ.get(key, 'NOT SET')}")


@app.get("/")
def root():
    return {"status": "ok"}
