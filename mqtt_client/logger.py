import logging


def _get_logger() -> logging.Logger:
    """Helper func to configure logger"""
    logger = logging.getLogger("MQTTClient")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


mqtt_logger = _get_logger()
