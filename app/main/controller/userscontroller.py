from flask_restx import Resource, Namespace, fields
from flask import request
from app.main.service.userservice import UsersService


api = Namespace("Usuarios", description="Gestao de Usuarios")

modelo = api.model(
    "UsersModel",
    {
        "username": fields.String(required=True, description="Nome de usuário"),
        "name": fields.String(required=True, description="Nome completo do usuário"),
    },
)


# Classe responsável pelas operações relacionadas à coleção de usuários (listar e criar usuários)
@api.route("/")
class UserController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self):
        # Retorna todos os usuários cadastrados
        return UsersService.obter(), 200

    @api.expect(modelo)
    @api.response(201, "Usuário Cadastrado")
    @api.response(400, "Operacao Invalidada")
    def post(self):
        # Cria um novo usuário com os dados fornecidos
        data = request.json
        if not data.get("username") or not data.get("name"):
            return {"mensagem": "Campos 'username' e 'name' sao obrigatorios"}, 400
        return UsersService.adicionar(data), 201


# Classe responsável pelas operações relacionadas a um usuário específico (buscar, atualizar e deletar por ID)
@api.route("/<int:id>")
class UserIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    @api.response(404, "Usuário não encontrado")
    def get(self, id):
        # Retorna os dados de um usuário específico pelo ID
        user = UsersService.obterbyid(id)
        if not user:
            return {"mensagem": "Usuário não encontrado"}, 404
        return user, 200

    @api.expect(modelo)
    @api.response(201, "Usuário atualizado com sucesso")
    @api.response(400, "Dados inválidos")
    @api.response(404, "Usuário não encontrado")
    def put(self, id):
        # Atualiza os dados de um usuário específico pelo ID
        data = request.json
        if not data.get("name") and not data.get("username"):
            return {"mensagem": "Informe ao menos 'name' ou 'username'"}, 400

        resultado = UsersService.alterar(id, data)
        if "não encontrado" in resultado["mensagem"]:
            return resultado, 404
        return resultado, 201

    @api.response(200, "Usuário deletado com sucesso")
    @api.response(404, "Usuário não encontrado")
    def delete(self, id):
        # Remove um usuário específico pelo ID
        resultado = UsersService.remover(id)
        if "não encontrado" in resultado["mensagem"]:
            return resultado, 404
        return resultado, 200
