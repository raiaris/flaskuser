from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from app.main.db.db import db


class Base(DeclarativeBase):
    pass


class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)

    print("Create Users Table")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
        }

    def insert_data(self, user):
        self.name.data = user.name
        self.username.data = user.username
