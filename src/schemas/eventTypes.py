from beanie import Document, Insert, before_event
import secrets
from enum import IntEnum
from pydantic import BaseModel,EmailStr,Field,model_validator
class eventType(IntEnum):
    ADD=1
    DELETE=2

class orderSchema(Document):
    dishes:list[int]
    order_id:int|None
    table_id:int

class OrderInputType(BaseModel):
    dishes:list[int]
    table_id:int
    event_type:eventType

