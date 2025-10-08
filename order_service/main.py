from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .database import Base, engine, SessionLocal
from .models import Order, Product, OrderItem
from .schemas import AddItemRequest, OrderItemResponse
from typing import List

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Order Service (PostgreSQL)")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/orders/{order_id}/items")
def add_item_to_order(order_id: int, request: AddItemRequest, db: Session = Depends(get_db)):
    order = db.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    product = db.get(Product, request.product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if product.quantity < request.quantity:
        raise HTTPException(status_code=400, detail="Not enough product in stock")

    order_item = db.query(OrderItem).filter_by(order_id=order_id, product_id=request.product_id).first()

    if order_item:
        order_item.quantity += request.quantity
    else:
        order_item = OrderItem(
            order_id=order_id,
            product_id=request.product_id,
            quantity=request.quantity,
            price=product.price
        )
        db.add(order_item)

    product.quantity -= request.quantity
    db.commit()

    return {"message": "Product added to order successfully"}


@app.get("/order-items", response_model=List[OrderItemResponse])
def get_all_order_items(db: Session = Depends(get_db)):
    return db.query(OrderItem).all()
