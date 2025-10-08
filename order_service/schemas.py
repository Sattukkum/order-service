from pydantic import BaseModel


class AddItemRequest(BaseModel):
    product_id: int
    quantity: int


class OrderItemResponse(BaseModel):
    order_id: int
    product_id: int
    quantity: int
    price: float

    class Config:
        orm_mode = True
