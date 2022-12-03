from fastapi import FastAPI

from healthcheck.api import healthcheck_router


def healthcheck_routes(app: FastAPI) -> None:
    app.include_router(healthcheck_router)
