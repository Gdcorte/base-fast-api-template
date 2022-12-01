from typing import Any, Dict

from flask import request
from flask_restful import Resource

from lib.api.models import BaseResponseModel
from lib.exceptions import BaseErpException


class BaseResourceException(BaseErpException):
    pass


class BadRequestException(BaseResourceException):
    def __init__(self, *args: object) -> None:
        super().__init__("Incorrect Parameters passed", *args)


class ProtectedResourceException(BaseResourceException):
    pass


class InvalidTokenException(ProtectedResourceException):
    pass


class InvalidAccessScopeException(ProtectedResourceException):
    pass


class InvalidAccessRightsException(ProtectedResourceException):
    pass


class BaseResource(Resource):
    def get_request_body(self) -> Dict[str, Any]:
        body = request.get_json()
        if not body:
            raise BadRequestException()

        return body

    def get_query_params(self) -> Dict[str, Any]:
        params = request.args

        return params

    def return_with_code(self, response: BaseResponseModel, status_code: int = 200):

        return (
            response.json(),
            status_code,
        )


class ProtectedResource(BaseResource):
    pass


class FilteredProtectedResource(ProtectedResource):
    pass
