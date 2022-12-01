from json import loads

from flask.testing import FlaskClient

from lib.api.models import BaseResponseModel


def test_healthcheck(mock_client: FlaskClient):
    response = mock_client.get("/healthcheck")

    assert response.status_code == 200
    response_body = response.get_json()
    assert response_body

    body = BaseResponseModel.parse_obj(loads(response_body))

    assert body.message == "Check!"
