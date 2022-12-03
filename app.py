from os import environ, getenv

from dotenv import load_dotenv
from fastapi import FastAPI
from flask import Flask
from flask_restful import Api

from healthcheck import healthcheck_routes


# Preconfigure app
def prepare_environment():
    environ["CONNECTION_METHOD"] = "ENV_FILE"
    load_dotenv()


def prepare_app():
    prepare_environment()

    # myApp = Flask(__name__)

    # # Configure e-mail settings
    # myApp.config["MAIL_SERVER"] = getenv("MAIL_SERVER")
    # myApp.config["MAIL_PORT"] = getenv("MAIL_PORT")
    # myApp.config["MAIL_USERNAME"] = getenv("MAIL_USERNAME")
    # myApp.config["MAIL_PASSWORD"] = getenv("MAIL_PASSWORD")
    # myApp.config["MAIL_USE_TLS"] = getenv("MAIL_USE_TLS", "") == "True"
    # myApp.config["MAIL_USE_SSL"] = getenv("MAIL_USE_SSL", "") == "True"

    # api = Api(myApp)
    # healthcheck_routes(api)

    app = FastAPI()
    healthcheck_routes(app)

    return app
