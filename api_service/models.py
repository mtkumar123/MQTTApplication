from typing import TypedDict

from pydantic import BaseModel, Field


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
    """
    Model used for API Response for
    payload found in published message
    """

    session_id: int = Field(description="Session ID")
    energy_delivered_kwh: int = Field(description="Energy Delivered in KWh")
    duration_seconds: int = Field(description="Duration in seconds")
    cost_cents: int = Field(description="Cost in cents")


class Message(BaseModel):
    payload: Payload
    timestamp: float
    topic: str
