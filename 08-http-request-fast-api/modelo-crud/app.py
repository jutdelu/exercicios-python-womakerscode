from fastapi import FastAPI, HTTPException
from uuid import UUID, uuid4
from typing import List
from models import User, Role

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("df8a2e24-ec44-4b28-9777-2fb69b71590f"),
        first_name="Ana",
        last_name="Maria",
        email="email@gmail.com",
        role=[Role.role_1]
    ),
    User(
        id=UUID("e7689585-ccf8-4283-bea0-b76a25669169"),
        first_name="Juliana", 
        last_name="Torres", 
        email="email@gmail.com", 
        role=[Role.role_2]
    ),
    User(
        id=UUID("10e5d8a1-59cb-439c-b2d5-d6d050a8ca1c"),
        first_name="Leticia", 
        last_name="Torres", 
        email="email@gmail.com", 
        role=[Role.role_3]
    ),

]

@app.get("/")
async def root():
    return {"mensage": "Olá, woMakers!"}

@app.get("/api/users")
async def get_users():
    return db

@app.get("/api/users/{id}")
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message": "Usuário não encontrado!"}

@app.post("/api/users")
async def add_user(user: User):
    db.append(user)
    return{"id": user.id}

@app.delete("/api/users/{id}")
async def remove_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com o id {id} não encontrado!"
    )    
