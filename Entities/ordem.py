from fastapi import FastAPI

app = FastAPI()

# A ordem das operações importa
@app.get("/users/me")  # rota para pegar dados do usuário atual
async def root_user_me():  
    return {"user-id" : "The current user"}  

@app.get("/users/{user_id}")  # rota para pegar dados de um usuário especifico
async def root_user(user_id: str):  # caso essa operação venha antes da operação para pegar o usuário atual. Ela receberá o valor "me"
    return {"user-id" : user_id}
