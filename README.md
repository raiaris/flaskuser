# Documentação do Projeto

## Requisitos

Antes de iniciar, certifique-se de ter os seguintes requisitos instalados:

- Python 3.x
- pip (gerenciador de pacotes do Python)
- Virtualenv (opcional, mas recomendado)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)

Você pode instalar as dependências do projeto utilizando o arquivo `requirements.txt`:


## Instalação de Dependências

Execute o comando abaixo para instalar as dependências do projeto:

```bash
pip install -r requirements.txt
```

---

## Project Organization

```
crudflask/
│
├── app/
│   ├── main/
│   │   ├── controller/      # Controllers das rotas da API
│   │   │   └── userscontroller.py
│   │   ├── model/           # Modelos do banco de dados
│   │   │   └── users.py
│   │   ├── service/         # Lógica de negócio (services)
│   │   │   └── userservice.py
│   │   └── __init__.py
│   └── db/                  # Configuração do banco de dados
│       └── db.py
├── requirements.txt         # Dependências do projeto
├── README.md
└── run.py                   # Ponto de entrada da aplicação Flask
```

---

## Inicializando o Banco de Dados com Flask-Migrate

Siga os passos abaixo para configurar e iniciar o banco de dados localmente utilizando o Flask-Migrate:

1. **Abra o terminal na raiz do projeto.**

2. **Inicialize o diretório de migrações (apenas na primeira vez):**
   ```bash
   flask db init
   ```

3. **Gere um arquivo de migração com base nas alterações do modelo:**
   ```bash
   flask db migrate -m "Mensagem descritiva da migração"
   ```

4. **Aplique as migrações ao banco de dados:**
   ```bash
   flask db upgrade
   ```

Esses comandos irão criar as tabelas e estruturas necessárias no banco de dados definido na configuração do seu projeto Flask.

---

## Documentação das Rotas da API

A API está documentada automaticamente via Swagger em `/swagger`.

### Endpoints Disponíveis

#### Listar todos os usuários
- **GET** `/usuarios/`
- **Resposta:** 200 OK  
  ```json
  [
    {
      "id": 1,
      "username": "usuario1",
      "name": "Nome Completo"
    }
  ]
  ```

#### Criar um novo usuário
- **POST** `/usuarios/`
- **Body:**  
  ```json
  {
    "username": "novousuario",
    "name": "Nome do Usuário"
  }
  ```
- **Resposta:** 201 Created  
  ```json
  {
    "mensagem": "Usuario Adicionado"
  }
  ```

#### Buscar usuário por ID
- **GET** `/usuarios/<id>`
- **Resposta:** 200 OK  
  ```json
  {
    "id": 1,
    "username": "usuario1",
    "name": "Nome Completo"
  }
  ```
- **Resposta se não encontrado:** 404  
  ```json
  {
    "mensagem": "Usuário não encontrado"
  }
  ```

#### Atualizar usuário por ID
- **PUT** `/usuarios/<id>`
- **Body:**  
  ```json
  {
    "username": "novonome",
    "name": "Novo Nome"
  }
  ```
- **Resposta:** 201  
  ```json
  {
    "mensagem": "Usuário <id> atualizado com sucesso"
  }
  ```

#### Remover usuário por ID
- **DELETE** `/usuarios/<id>`
- **Resposta:** 200  
  ```json
  {
    "mensagem": "Usuario <id> Deletado"
  }
  ```
- **Resposta se não encontrado:** 404  
  ```json
  {
    "mensagem": "Usuário <id> não encontrado"
  }
  ```

---

## Como Utilizar a API

Você pode testar as rotas utilizando ferramentas como [Postman](https://www.postman.com/) ou [curl](https://curl.se/).  
Exemplo usando `curl` para criar um usuário:

```bash
curl -X POST http://localhost:5000/usuarios/ \
     -H "Content-Type: application/json" \
     -d '{"username": "usuarioapi", "name": "Nome API"}'
```

---

## Observações

- Para mais informações, consulte a [documentação oficial do Flask-Migrate](https://flask-migrate.readthedocs.io/).
- Os métodos estão documentados no localhost, utilizando o Swagger para facilitar o teste.