from fastapi import FastAPI

app = FastAPI(title="Catalog Service")

items = [
    {"id": 1, "name": "Item A"},
    {"id": 2, "name": "Item B"}
]

@app.get("/items")
async def get_items():
    return items
