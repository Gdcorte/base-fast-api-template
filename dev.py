import logging
import sys
from logging import DEBUG

from app import prepare_app


def configure_root_logger():
    root_log = logging.getLogger()

    formatter = logging.Formatter("[%(levelname)s] %(message)s")

    log_handler = logging.StreamHandler(stream=sys.stdout)
    log_handler.setFormatter(formatter)
    log_handler.setLevel(DEBUG)

    root_log.addHandler(log_handler)
    root_log.setLevel(DEBUG)

    root_log.debug("Starting in debug mode")


if __name__ == "__main__":
    configure_root_logger()
    app = prepare_app()

    app.run(debug=True, host="0.0.0.0")
