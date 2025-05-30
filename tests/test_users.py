import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

from app.main.controller.userscontroller import api as users_ns
from app.main.model.users import Users
from app.main.service.userservice import UsersService
from app.main.db.db import db as _db


@pytest.fixture
def app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    _db.init_app(app)

    api = Api(app)
    api.add_namespace(users_ns, path="/usuarios")

    with app.app_context():
        _db.create_all()
        yield app

## Testes para validar sucesso 200/201

@pytest.fixture
def client(app):
    return app.test_client()


def test_post_user(client):
    response = client.post(
        "/usuarios/", json={"username": "raiaris", "name": "Rai Sousa Aris"}
    )
    assert response.status_code == 201


def test_get_all_users(client):
    client.post("/usuarios/", json={"username": "raiaris", "name": "Rai Sousa Aris"})
    response = client.get("/usuarios/")
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_get_user_by_id(client):
    client.post("/usuarios/", json={"username": "raiaris", "name": "Rai Sousa Aris"})
    response = client.get("/usuarios/1")
    assert response.status_code == 200


def test_put_user(client):
    client.post("/usuarios/", json={"username": "raiaris", "name": "Rai Sousa Aris"})
    response = client.put("/usuarios/1", json={"name": "Rai Atualizado"})
    assert response.status_code == 201


def test_delete_user(client):
    client.post("/usuarios/", json={"username": "raiaris", "name": "Rai Sousa Aris"})
    response = client.delete("/usuarios/1")
    assert response.status_code == 200

### Testes para validar erros 400/404

def test_post_user_missing_username(client):
    response = client.post("/usuarios/", json={"name": "Rai Sousa Aris"})
    assert response.status_code == 400


def test_post_user_missing_name(client):
    response = client.post("/usuarios/", json={"username": "raiaris"})
    assert response.status_code == 400


def test_get_user_not_found(client):
    response = client.get("/usuarios/9999")
    assert response.status_code == 404


def test_put_user_not_found(client):
    response = client.put("/usuarios/9999", json={"name": "Nome Novo"})
    assert response.status_code == 404


def test_put_user_invalid_data(client):
    client.post("/usuarios/", json={"username": "raiaris", "name": "Rai Sousa Aris"})
    response = client.put("/usuarios/1", json={"name": None})
    assert response.status_code == 400


def test_delete_user_not_found(client):
    response = client.delete("/usuarios/9999")
    assert response.status_code == 404
