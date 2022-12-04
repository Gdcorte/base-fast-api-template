from fastapi_restful.cbv import cbv
from fastapi_restful.inferring_router import InferringRouter

from lib.api.models import BaseResponseModel
from lib.api.resources import BaseResource

healthcheck_router = InferringRouter(
    prefix="/healthcheck",
)


@cbv(healthcheck_router)
class Api(BaseResource):
    """Healthcheck class resource"""

    @healthcheck_router.get("/")
    async def get(self) -> BaseResponseModel:
        """
        This endpoint will simply return 200.
        It means the server is active and ready to take requests.
        In case something other than 200 is returned, there is an error.
        """

        response_body = BaseResponseModel(message="Check!")
        return response_body
