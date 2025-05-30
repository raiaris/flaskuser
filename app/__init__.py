from flask import Flask, Blueprint
from flask_restx import Api


from app.main.controller.userscontroller import api as home_ns


from app.main.db import db, migrate


app = Flask(__name__)
blueprint = Blueprint("api", __name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

app.register_blueprint(blueprint)

authorizations = {
    "bearer": {
        "name": "Authorization",
        "in": "header",
        "type": "apiKey",
        "description": "Insert your JWT Token here!",
    }
}
api = Api(
    app,
    title="Rai Aris Swagger Api Users Model",
    version="1.0",
    description="Teste Pratico PICPAY",
    prefix="/api",
    authorizations=authorizations,
)


api.add_namespace(home_ns, path="/users")
db.configure(app)
migrate.configure(app)
