from typing import List
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: int

class ListProduct(BaseModel):
    products: List[Product]