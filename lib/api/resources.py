from flask_restful import Resource

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
    pass


class ProtectedResource(BaseResource):
    pass


class FilteredProtectedResource(ProtectedResource):
    pass
