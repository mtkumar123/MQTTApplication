from typing import TypedDict

from pydantic import BaseModel


class PayloadDictType(TypedDict):
    session_id: int
    energy_delivered_kwh: int
    duration_seconds: int
    cost_cents: int


class MessageDictType(TypedDict):
    payload: PayloadDictType
    timestamp: float
    topic: str


class Payload(BaseModel):
    session_id: int
    energy_delivered_kwh: int
    duration_seconds: int
    cost_cents: int


class Message(BaseModel):
    payload: Payload
    timestamp: float
    topic: str
