from fastapi import FastAPI

app = FastAPI()

# @algumacoisa é chamado de decorador
@app.get("/")  # Esse decorador informa que a função abaixo pertence a rota / com uma operação get
async def root():
    return {"message" : "Hello worldo"}

# input do console: uvicorn main:app --reload
# main = nome do arquivo .py
# app = instancia de FastAPI
# --reload = faz o servidor reiniciar após mudanças no código
