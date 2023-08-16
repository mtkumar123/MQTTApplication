from random import randint

from pydantic import BaseModel, ConfigDict, Field
from pymongo import MongoClient


def _get_random_int() -> int:
    return randint(0, 100)


class UserData(BaseModel):
    """
    Model used as UserData for mqtt client
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    client_id: str
    db_conn: MongoClient
    db_collection: str
    db_name: str
    topic: str


class Payload(BaseModel):
    """
    Model for payload of message received
    from Broker
    """

    session_id: int
    energy_delivered_kwh: int = Field(default_factory=_get_random_int)
    duration_seconds: int = Field(default_factory=_get_random_int)
    cost_cents: int = Field(default_factory=_get_random_int)


class Message(BaseModel):
    """
    Model to store payload along with
    topic and timestamp in DB
    """

    payload: Payload
    timestamp: float
    topic: str
