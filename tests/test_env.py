import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ENV_KEYS = [
    "MY_VARIABLE",
]


def test_something(caplog):
    for key in ENV_KEYS:
        logger.info(f"{key}={os.environ.get(key, 'NOT SET')}")
