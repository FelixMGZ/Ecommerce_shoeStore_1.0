from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    price: float
    size: int
    quantity: int
    gender: Optional[str] = None
    img_url: str

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: str