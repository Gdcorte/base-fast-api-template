from lib.api.models import BaseResponseModel
from lib.api.resources import BaseResource


class Api(BaseResource):
    """Healthcheck API Resource"""

    def get(self):
        response_body = BaseResponseModel(message="Check!")
        return self.return_with_code(response_body)
