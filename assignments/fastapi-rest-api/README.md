# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Aprender a criar uma API REST simples utilizando o framework FastAPI em Python. O estudante irá construir endpoints, manipular dados e executar a aplicação localmente.

## 📝 Tasks

### 🛠️ Criar um endpoint GET

#### Description
Implemente um endpoint GET que retorne uma mensagem de boas-vindas em formato JSON.

#### Requirements
Completed program should:

- Ter um endpoint `/` que responda a requisições GET
- Retornar um JSON com uma mensagem de boas-vindas
- Utilizar FastAPI para definir o endpoint


### 🛠️ Criar um endpoint POST para cadastro

#### Description
Implemente um endpoint POST `/cadastro` que receba dados de um usuário (nome e idade) e retorne esses dados em formato JSON.

#### Requirements
Completed program should:

- Ter um endpoint `/cadastro` que aceite requisições POST
- Receber um JSON com os campos `nome` e `idade`
- Retornar os dados recebidos em formato JSON
- Utilizar FastAPI e Pydantic para validação dos dados


### 🛠️ (Opcional) Listar usuários cadastrados

#### Description
Implemente um endpoint GET `/usuarios` que retorne uma lista dos usuários cadastrados durante a execução da aplicação.

#### Requirements
Completed program should:

- Ter um endpoint `/usuarios` que responda a requisições GET
- Retornar uma lista de usuários cadastrados
- Armazenar os usuários em uma lista em memória
