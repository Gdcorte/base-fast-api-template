from fastapi.testclient import TestClient

from lib.api.models import BaseResponseModel


def test_healthcheck(mock_client: TestClient):
    response = mock_client.get("/healthcheck")

    assert response.status_code == 200

    response_body = response.json()
    assert response_body

    body = BaseResponseModel.parse_obj(response_body)

    assert body.message == "Check!"
