from typing import Any, Dict

from fastapi import FastAPI

from healthcheck.api import healthcheck_router


def healthcheck_openapi_tags() -> Dict[str, Any]:
    return {
        "name": "Healthcheck",
        "description": "Check if the server is running.",
    }


def healthcheck_routes(app: FastAPI) -> None:
    app.include_router(healthcheck_router, tags=["Healthcheck"])
