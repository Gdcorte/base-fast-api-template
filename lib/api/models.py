from pydantic import BaseModel, Extra


class BaseResponseModel(BaseModel, extra=Extra.allow):
    message: str
