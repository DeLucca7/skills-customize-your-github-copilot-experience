from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modelo para cadastro de usuário
class Usuario(BaseModel):
    nome: str
    idade: int

# Lista em memória para armazenar usuários cadastrados
usuarios: List[Usuario] = []

@app.get("/")
def boas_vindas():
    return {"mensagem": "Bem-vindo à API FastAPI!"}

@app.post("/cadastro")
def cadastrar_usuario(usuario: Usuario):
    usuarios.append(usuario)
    return usuario

@app.get("/usuarios")
def listar_usuarios():
    return usuarios
