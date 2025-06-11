from pydantic import BaseModel
from typing import List

class OrderItem(BaseModel):
    name: str
    price: float

class OrderCreate(BaseModel):
    user_email: str
    items: List[OrderItem]
    total: float
    date: str
    status: str