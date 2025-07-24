import uvicorn

from src.api import app
from src.core import settings


def main():
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=settings.PORT,
        log_level="info",
    )
