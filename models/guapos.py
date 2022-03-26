from flask_login.mixins import UserMixin
from db.db_engine import db


class Guapos(db.Model, UserMixin):  # type: ignore

    # campos
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    apellido = db.Column(db.String(30), nullable=False)
    guapura = db.Column(db.Integer, nullable=True)
    soltero = db.Column(db.Boolean, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    ispapucho = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, apellido, guapura, soltero, password, ispapucho) -> None:

        self.name = name
        self.apellido = apellido
        self.guapura = guapura
        self.soltero = soltero
        self.password = password
        self.ispapucho = ispapucho

    def __repr__(self):
        return f"""{self.name}, {self.apellido}, {self.guapura}, {self.ispapucho}"""
    
