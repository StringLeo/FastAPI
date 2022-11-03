from enum import Enum
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):  # Parametros de consulta
    return fake_items_db[skip : skip + limit]

# skip = quantidade de indices que ele ignora/pula
# limit = quantidade de indices que ele lê