from fastapi_restful.cbv import cbv
from fastapi_restful.inferring_router import InferringRouter

from lib.api.models import BaseResponseModel
from lib.api.resources import BaseResource

healthcheck_router = InferringRouter(
    prefix="/healthcheck",
)


@cbv(healthcheck_router)
class Api(BaseResource):
    """Healthcheck API Resource"""

    @healthcheck_router.get("/")
    async def get(self) -> BaseResponseModel:
        response_body = BaseResponseModel(message="Check!")
        return response_body
