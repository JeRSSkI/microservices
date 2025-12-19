from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Orders Service")

orders = []
order_id_seq = 1

class OrderRequest(BaseModel):
    userId: int
    itemId: int
    qty: int

@app.post("/orders", status_code=201)
async def create_order(order: OrderRequest):
    global order_id_seq
    new_order = {"id": order_id_seq, **order.dict()}
    orders.append(new_order)
    order_id_seq += 1
    return new_order
