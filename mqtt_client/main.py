import time

import config
import models
import utils

topic = "charger/1/connector/1/session/1"
client_id = "Client1"
settings = config.get_settings()
mqtt_broker_url = settings.mqtt_broker_url
mqtt_broker_port = settings.mqtt_broker_port

if __name__ == "__main__":
    client = utils.get_client(client_id=client_id)
    utils.start_connection(client, mqtt_broker_url, mqtt_broker_port)
    utils.configure_subscriptions(client, topic)
    while True:
        payload = models.Payload(
            session_id=1,
        )
        result = client.publish(
            topic=topic,
            payload=payload.model_dump_json(),
        )
        time.sleep(2)
