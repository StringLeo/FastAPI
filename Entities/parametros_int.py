from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):  # item_id recebe o valor presente na rota /items/
    return {"item-id" : item_id}
