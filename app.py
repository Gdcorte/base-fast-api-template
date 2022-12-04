from os import environ

from dotenv import load_dotenv
from fastapi import FastAPI

from healthcheck import healthcheck_routes
from healthcheck.routes import healthcheck_openapi_tags


# Preconfigure app
def prepare_environment():
    environ["CONNECTION_METHOD"] = "ENV_FILE"
    load_dotenv()


def prepare_app():
    prepare_environment()

    tags = [healthcheck_openapi_tags()]

    app = FastAPI(
        title="ERP System - Backend",
        description="ERP System",
        version="0.0.1",
        terms_of_service="http://coming.soon.com",
        contact={
            "name": "Gustavo & Julio",
            "url": "http://gdcorte.com",
            "email": "quiezidiniz@gmail.com",
        },
        license_info={
            "name": "Apache 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        },
        openapi_tags=tags,
        # openapi_url=None,
    )
    healthcheck_routes(app)

    return app
