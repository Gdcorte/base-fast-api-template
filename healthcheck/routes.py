from flask_restful import Api as FlaskApi

from healthcheck.api import Api


def healthcheck_routes(api: FlaskApi) -> None:
    api.add_resource(Api, "/healthcheck")
