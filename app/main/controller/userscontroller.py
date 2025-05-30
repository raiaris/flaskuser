from flask_restx import Resource, Namespace, fields
from flask import request
from app.main.service.userservice import UsersService

api = Namespace("Usuarios", description="Gestao de Usuarios")
modelo = api.model("UsersModel", {"username": fields.String, "name": fields.String})


@api.route("/")
class UserController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self):
        return UsersService.obter(), 200

    @api.expect(modelo)
    def post(self):
        return UsersService.adicionar(request.json), 201


@api.route("/<id>")
class UserIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id: int):
        return UsersService.obterbyid(int(id)), 200

    @api.response(200, "Busca realizada com sucesso")
    @api.expect(modelo)
    def put(self, id: int):
        return UsersService.alterar(int(id), request.json), 201

    def delete(self, id: int):
        return UsersService.remover(int(id)), 200
