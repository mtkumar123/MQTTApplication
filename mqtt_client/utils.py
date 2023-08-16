import json
import logging

import crud
import models
import paho.mqtt.client as mqtt


def _get_logger():
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


logger = _get_logger()


def on_connect(client: mqtt.Client, userdata, flags: dict, rc: int) -> None:
    logger.info(f"{userdata['client_id']} has connected to broker")


def on_disconnect(client: mqtt.Client, userdata, rc) -> None:
    logger.info(
        f"{userdata['client_id']} has disconnected from broker with {rc}"
    )


def on_message(
    client: mqtt.Client, userdata: dict, message: mqtt.MQTTMessage
) -> None:
    payload: dict = json.loads(bytes.decode(message.payload))
    logger.info(f"{userdata['client_id']} has recieved a message.")
    logger.info(f"Message timestamp - {message.timestamp}")
    logger.info(f"Message payload - {payload}")
    data = models.Message(
        payload=payload,
        topic=message.topic,
        timestamp=message.timestamp,
    )
    crud.insert_document(data)


def on_publish(client: mqtt.Client, userdata: dict, mid: int) -> None:
    logger.info(f"{userdata['client_id']} has published a message")


def get_client(client_id: str) -> mqtt.Client:
    client = mqtt.Client(
        client_id=client_id, userdata={"client_id": client_id}
    )
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.on_publish = on_publish
    return client


def start_connection(client: mqtt.Client, url: str, port: int) -> None:
    try:
        client.connect(host=url, port=port)
        client.loop_start()
    except Exception:
        logger.exception("Unable to connect to broker")
        raise


# should we add support for other QoS
def configure_subscriptions(client: mqtt.Client, topic: str) -> None:
    try:
        client.subscribe(topic=topic, qos=0)
    except Exception:
        logger.exception(f"Unable to subscribe to topic - {topic}")
        raise


def publish_message(client: mqtt.Client, topic: str, payload: str) -> None:
    try:
        client.publish(topic, payload)
    except Exception:
        logger.exception("Unable to publish message")
