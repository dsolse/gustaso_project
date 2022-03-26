from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from db.db_engine import db
from models.guapos import Guapos
from routes.auth import auth
from routes.vip import vip
from db.login import login_manager
from flask_migrate import Migrate
from db.db_engine import db

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

app.register_blueprint(auth)
app.register_blueprint(vip)

# Intercepcion de mundos a la db dando settings
SQLAlchemy(app)
Bcrypt(app)
login_manager.init_app(app)
Migrate(app, db)

# creando las tablas con los settings dados
with app.app_context():
    db.create_all()


if "__main__" == __name__:
    app.run(debug=True)
