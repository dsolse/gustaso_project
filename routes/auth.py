from flask import Blueprint
from flask.helpers import url_for
from flask.templating import render_template
from flask_login.utils import logout_user
from werkzeug.utils import redirect

from forms.form_register import RegisterForm
from models.guapos import Guapos
from forms.form_login import LoginForm
from db.db_engine import db
from db.bcrypt import bcrypt
from flask_login import login_user


auth = Blueprint("auth", __name__)


@auth.route("/")
def home():
    if not Guapos.query.filter_by(apellido="algas").first():
        password_hash = bcrypt.generate_password_hash("123")
        el_papucho = Guapos("balbino", "algas", 10, 1, password_hash, True)
        db.session.add(el_papucho)
        db.session.commit()
    return render_template("auth.html")


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.home"))


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        apellido = form.apellido.data
        passw = form.password.data
        user = Guapos.query.filter_by(apellido=apellido).first()
        if user:
            if bcrypt.check_password_hash(user.password, passw):
                login_user(user)
                return redirect(url_for("vip.home"))
    return render_template("login.html", form=form)


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        name = form.name.data
        apellido = form.apellido.data
        passsword = form.password.data
        passsword_hashed = bcrypt.generate_password_hash(passsword)
        soltero = True if form.soltero.data == "1" else False

        newGuapo = Guapos(name, apellido, None, soltero, passsword_hashed)
        db.session.add(newGuapo)
        db.session.commit()
        return redirect(url_for("auth.login"))

    return render_template("register.html", form_register=form)
