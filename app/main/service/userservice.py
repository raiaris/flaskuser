from app.main.db.db import db
from app.main.model.users import Users


class UsersService:

    @classmethod
    def adicionar(cls, item):
        user = Users(name=item["name"], username=item["username"])
        db.session.add(user)
        db.session.commit()
        if user:
            db.session.add(user)
            db.session.commit()
            return {"mensagem": f"Usuario Adicionado"}, 200
        else:
            return {"mensagem": f"Usuário {id} não adicionado"}, 404

    @classmethod
    def obter(cls):
        return [user.to_dict() for user in Users.query.all()]

    @classmethod
    def obterbyid(cls, id):
        user = Users.query.filter_by(id=id).first()
        if user:
            return user.to_dict(), 200
        else:
            return {"mensagem": f"Usuário {id} não encontrado"}, 404

    @classmethod
    def remover(cls, id):
        user = Users.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return {"mensagem": f"Usuario {id} Deletado"}, 200
        else:
            return {"mensagem": f"Usuário {id} não encontrado"}, 404

    @classmethod
    def alterar(cls, id, item):
        user = Users.query.filter_by(id=id).first()
        if not user:
            return {"mensagem": f"Usuário {id} não encontrado"}, 404

        if "name" in item:
            user.name = item["name"]
        if "username" in item:
            user.username = item["username"]

        db.session.commit()
        return {"mensagem": f"Usuário {id} atualizado com sucesso"}
