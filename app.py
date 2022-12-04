from os import environ

from dotenv import load_dotenv
from fastapi import FastAPI

from healthcheck import healthcheck_routes


# Preconfigure app
def prepare_environment():
    environ["CONNECTION_METHOD"] = "ENV_FILE"
    load_dotenv()


def prepare_app():
    prepare_environment()

    app = FastAPI()
    healthcheck_routes(app)

    return app
