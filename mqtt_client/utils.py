import json

import crud
import models
import paho.mqtt.client as mqtt
from logger import mqtt_logger


def on_connect(
    client: mqtt.Client, userdata: models.UserData, flags: dict, rc: int
) -> None:
    """Callback function after connection to broker is completed.

    :param mqtt.Client client
    :param _type_ userdata
    :param dict flags
    :param int rc
    """
    mqtt_logger.info(f"{userdata.client_id} has connected to broker")
    configure_subscriptions(client, userdata.topic)


def on_disconnect(
    client: mqtt.Client, userdata: models.UserData, rc: int
) -> None:
    """Callback function when connection to broker is lost.

    :param mqtt.Client client
    :param _type_ userdata
    :param _type_ rc
    """
    mqtt_logger.info(
        f"{userdata.client_id} has disconnected from broker with {rc}"
    )


def on_message(
    client: mqtt.Client, userdata: models.UserData, message: mqtt.MQTTMessage
) -> None:
    """Callback function when client receives message from broker from
    a subscription. Function logs message and inserts message into db.

    :param mqtt.Client client
    :param dict userdata
    :param mqtt.MQTTMessage message
    """
    payload: dict = json.loads(bytes.decode(message.payload))
    mqtt_logger.info(f"{userdata.client_id} has recieved a message.")
    mqtt_logger.info(f"Message timestamp - {message.timestamp}")
    mqtt_logger.info(f"Message payload - {payload}")
    data = models.Message(
        payload=payload,
        topic=message.topic,
        timestamp=message.timestamp,
    )
    crud.insert_document(
        userdata.db_conn,
        userdata.db_name,
        userdata.db_collection,
        data,
    )


def on_publish(
    client: mqtt.Client, userdata: models.UserData, mid: int
) -> None:
    """Callback function after client publishes message.

    :param mqtt.Client client
    :param dict userdata
    :param int mid
    """
    mqtt_logger.info(f"{userdata.client_id} has published a message")


def get_client(userdata: models.UserData) -> mqtt.Client:
    """Helper function to configure client

    :param str client_id
    :return mqtt.Client
    """
    client = mqtt.Client(
        client_id=userdata.client_id,
        userdata=userdata,
    )
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.on_publish = on_publish
    return client


def start_connection(client: mqtt.Client, url: str, port: int) -> None:
    """Helper function to start connection to broker and start
    network loop

    :param mqtt.Client client
    :param str url: broker url
    :param int port: broker port
    """
    try:
        client.connect(host=url, port=port)
    except Exception:
        mqtt_logger.exception("Unable to connect to broker")
        raise
    client.loop_start()


# should we add support for other QoS
def configure_subscriptions(client: mqtt.Client, topic: str) -> None:
    """Helper function to configure subscriptions for topics
    for client to broker.

    :param mqtt.Client client
    :param str topic
    """
    try:
        client.subscribe(topic=topic, qos=0)
    except Exception:
        mqtt_logger.exception(f"Unable to subscribe to topic - {topic}")
        raise


def publish_message(client: mqtt.Client, topic: str, payload: str) -> None:
    """Helper function to publish message to the broker for a specific
    topic

    :param mqtt.Client client
    :param str topic
    :param str payload
    """
    try:
        client.publish(topic, payload)
    except Exception:
        mqtt_logger.exception("Unable to publish message")
