from fastapi import FastAPI, HTTPException

app = FastAPI(title="Simple FastAPI CRUD")

# In-memory "database"
items = {}

# ------------------ CREATE ------------------
@app.post("/items/")
def create_item(item_id: int, name: str, description: str = None):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item_id] = {"name": name, "description": description}
    return {"msg": "Item created", "item": items[item_id]}

# ------------------ READ ------------------
@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.get("/items/")
def list_items():
    return items

# ------------------ UPDATE ------------------
@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, description: str = None):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id].update({"name": name, "description": description})
    return {"msg": "Item updated", "item": items[item_id]}

# ------------------ DELETE ------------------
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = items.pop(item_id)
    return {"msg": "Item deleted", "item": deleted_item}
