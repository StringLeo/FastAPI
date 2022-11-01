from enum import Enum
from fastapi import FastAPI

app = FastAPI()

class modelName(str, Enum):  # Classe enumerator com modelos de machine learning
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: modelName):  # parametro do tipo modelName
    if model_name is modelName.alexnet:  # compara se o parametro da rota é igual a um atributo da classe modelName
        return {"model_name": model_name, "message" : "Deep learning FTW!"}

    if model_name.value == "lenet":  # compara se o valor recebido da rota é igual a string "lenet"
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name" : model_name, "message" : "Have some residuals"}  # retorna essa mensagem caso não caia em uma das condições anteriores
