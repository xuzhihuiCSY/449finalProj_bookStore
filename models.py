from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: Optional[str]
    title: str
    author: str
    description: str
    price: float
    stock: int
