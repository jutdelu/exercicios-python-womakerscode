# exercicios-python-womakerscode


Manipulando FastAPI

Criando ambiente de desenvolvimento

cria-se arquivo app.py

no terminal, digitar:

py -3 -m venv .venv

aguardar a criação da pasta

depois ativar, digitar:

.venv/Scripts/ativate
vai aparecer (.venv) ao lado do local do arquivo

instala flask, digitar:

pip Install Flask

espera instalar

depois roda, digitar:
flask  --app app run

Fast API

Iniciando no terminal:

py -3 -m venv .venv #ambiente virtual

.venv/Scripts/ativate #ativando ambiente

pip install "fastapi[all]” #instalando o fastapi

uvicorn app:app --reload  #rodando o app

Para acesso a documentação:

http://127.0.0.1:8000/docs #colocar doc ou redoc no fim da rota

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9f4a3238-c0b9-478b-97b5-44d82e5a8be9/159365d0-a3d1-48b0-8ba5-28a0865f2eba/Untitled.png)

Método GET

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9f4a3238-c0b9-478b-97b5-44d82e5a8be9/b7a18aeb-0b8f-4152-be57-f1f6494cfe7f/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9f4a3238-c0b9-478b-97b5-44d82e5a8be9/f4bca28c-7cea-4dbd-88c7-417941cf5d10/Untitled.png)

Método PUT

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9f4a3238-c0b9-478b-97b5-44d82e5a8be9/3e55a1cf-6e73-4dce-9399-3545db502656/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9f4a3238-c0b9-478b-97b5-44d82e5a8be9/4dfe90ec-efe2-411a-bad4-28cacb66658f/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9f4a3238-c0b9-478b-97b5-44d82e5a8be9/73b3ffec-d165-4636-9171-551f1b39f979/Untitled.png)

Modelo Crud

http://127.0.0.1:8000/api/users

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9f4a3238-c0b9-478b-97b5-44d82e5a8be9/e971b800-45d9-467c-a19f-59c4c8d871a0/Untitled.png)

Com esses ids, substitui-se o gerador de id pelo id gerado no navegador.

Antes era id=uuid4() #utilizado para a geração automática de id

Passa a ser id=UUID("df8a2e24-ec44-4b28-9777-2fb69b71590f"), por exemplo

Get USERS

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9f4a3238-c0b9-478b-97b5-44d82e5a8be9/a0eb6a61-7bd6-42b7-8c70-d894b1557c55/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9f4a3238-c0b9-478b-97b5-44d82e5a8be9/bf5052b2-0aaf-4863-91bd-ca2a1705ff0a/Untitled.png)

Utilizando o Thunder Client para manipulação

Método GET - para pegar o modelo de criação de usuário;

Método POST - para criar um usuário, retorna o id do novo usuário, de acordo com o descrito no código.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9f4a3238-c0b9-478b-97b5-44d82e5a8be9/785de01e-ecaf-444c-8f74-13246dfac06a/Untitled.png)

Método DELETE

Resposta null - removido com sucesso

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9f4a3238-c0b9-478b-97b5-44d82e5a8be9/aaf4da87-d866-4a65-b321-950a91bacca3/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9f4a3238-c0b9-478b-97b5-44d82e5a8be9/5ef67c76-3c6d-4b14-8eeb-c96be2209558/Untitled.png)

Tratamento de Exceção

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9f4a3238-c0b9-478b-97b5-44d82e5a8be9/e40ae055-0ed1-4d0d-8918-26a969976682/Untitled.png)
