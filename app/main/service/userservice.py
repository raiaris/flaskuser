from app.main.db.db import db
from app.main.model.users import Users


class UsersService:
    # Adiciona um novo usuário ao banco de dados
    @classmethod
    def adicionar(cls, item):
        user = Users(name=item["name"], username=item["username"])
        db.session.add(user)
        db.session.commit()
        return {"mensagem": "Usuario Adicionado"}

    # Retorna todos os usuários cadastrados
    @classmethod
    def obter(cls):
        return [user.to_dict() for user in Users.query.all()]

    # Busca um usuário pelo ID
    @classmethod
    def obterbyid(cls, id):
        user = Users.query.filter_by(id=id).first()
        return user.to_dict() if user else None

    # Remove um usuário pelo ID
    @classmethod
    def remover(cls, id):
        user = Users.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return {"mensagem": f"Usuario {id} Deletado"}
        else:
            return {"mensagem": f"Usuário {id} não encontrado"}

    # Atualiza os dados de um usuário pelo ID
    @classmethod
    def alterar(cls, id, item):
        user = Users.query.filter_by(id=id).first()
        if not user:
            return {"mensagem": f"Usuário {id} não encontrado"}
        if "name" in item:
            user.name = item["name"]
        if "username" in item:
            user.username = item["username"]
        db.session.commit()
        return {"mensagem": f"Usuário {id} atualizado com sucesso"}
