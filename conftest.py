import contextlib

import pytest
from flask import Flask

from app import prepare_app


@contextlib.contextmanager
def mock_app():
    app = prepare_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    yield app


@pytest.fixture()
def mock_client():
    with mock_app() as app:
        yield app.test_client()


@pytest.fixture()
def runner(app: Flask):
    with mock_app() as app:
        yield app.test_cli_runner()
