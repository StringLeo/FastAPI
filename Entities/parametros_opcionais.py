from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):  # q recebe o valor padrão None
    if q:
        return {"item-id" : item_id, "q" : q}  # 'q' é o parametro de consulta opcional
    return {"item-id" : item_id}
