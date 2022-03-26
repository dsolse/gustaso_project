from flask_login import LoginManager
from models.guapos import Guapos

login_manager = LoginManager()

login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(id):
    user = Guapos.query.get(id)
    return user
