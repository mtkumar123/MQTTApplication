import time

import config
import models
import utils
from pymongo import MongoClient

settings = config.get_settings()


def main() -> None:
    with MongoClient(settings.mongo_db_url, settings.mongo_db_port) as db_conn:
        userdata = models.UserData(
            db_conn=db_conn,
            db_collection=settings.collection_name,
            db_name=settings.db_name,
            client_id=settings.client_id,
            topic=settings.topic,
        )
        client = utils.get_client(
            userdata=userdata,
        )
        utils.start_connection(
            client,
            settings.mqtt_broker_url,
            settings.mqtt_broker_port,
        )
        while True:
            payload = models.Payload(
                session_id=1,
            )
            client.publish(
                topic=settings.topic,
                payload=payload.model_dump_json(),
            )
            time.sleep(settings.publish_interval)


if __name__ == "__main__":
    main()
