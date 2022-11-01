from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):  # item_id recebe o valor presente na rota /items/
    return {"item_id" : item_id} 
