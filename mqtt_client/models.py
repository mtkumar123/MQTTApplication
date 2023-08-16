from random import randint

from pydantic import BaseModel, Field


def _get_random_int() -> int:
    return randint(0, 100)


class Payload(BaseModel):
    session_id: int
    energy_delivered_kwh: int = Field(default_factory=_get_random_int)
    duration_seconds: int = Field(default_factory=_get_random_int)
    cost_cents: int = Field(default_factory=_get_random_int)


class Message(BaseModel):
    payload: Payload
    timestamp: float
    topic: str
