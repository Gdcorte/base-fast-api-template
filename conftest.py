import contextlib

import pytest
from fastapi.testclient import TestClient

from app import prepare_app


@contextlib.contextmanager
def mock_app():
    app = prepare_app()

    yield app


@pytest.fixture()
def mock_client():
    with mock_app() as app:
        yield TestClient(app)
