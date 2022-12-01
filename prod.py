import logging
import sys

from waitress import serve

from app import prepare_app


def configure_root_logger():
    root_log = logging.getLogger()

    formatter = logging.Formatter("[%(levelname)s] %(message)s")

    # TODO: Use a correct logging stream for production
    log_handler = logging.StreamHandler(stream=sys.stdout)
    log_handler.setFormatter(formatter)
    log_handler.setLevel(logging.INFO)

    root_log.addHandler(log_handler)
    root_log.setLevel(logging.INFO)

    root_log.debug("Starting in debug mode")


if __name__ == "__main__":
    configure_root_logger()
    app = prepare_app()

    serve(app, host="0.0.0.0", port=5000)
