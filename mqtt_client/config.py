from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Read in environment variables
    """

    mqtt_broker_url: str
    mqtt_broker_port: int
    mongo_db_url: str
    mongo_db_port: int
    db_name: str
    collection_name: str
    publish_interval: int
    topic: str = "charger/1/connector/1/session/1"
    client_id: str = "Client1"


@lru_cache
def get_settings() -> Settings:
    return Settings()
