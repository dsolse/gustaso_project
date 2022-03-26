from flask import Blueprint, url_for, redirect
from flask.templating import render_template
from flask_login import current_user
from flask_login.utils import login_required
from forms.form_guapo import GuapuraForm
from models.guapos import Guapos
from db.db_engine import db

vip = Blueprint("vip", __name__, url_prefix="/vip")


@vip.route("/")
@login_required
def home():
    return render_template("vip.html", user=current_user)


@vip.route("/guapos")
@login_required
def guapos():
    return render_template("home.html", user=current_user, rows=Guapos.query.all())


@vip.route("/change_guapura/<int:id_guapo>", methods=["GET", "POST"])
@login_required
def change_guapura(id_guapo):
    if current_user.ispapucho:
        form = GuapuraForm()
        guapo = Guapos.query.get(id_guapo)

        if form.validate_on_submit():
            guapo.apellido = form.apellido.data
            guapo.guapura = form.guapura.data
            db.session.add(guapo)
            db.session.commit()
            return redirect(url_for("vip.guapos"))

        form.apellido.data = guapo.apellido
        form.guapura.data = guapo.guapura
        

        return render_template("papucho_change.html", user=guapo, form=form) 
    else:
        return redirect(url_for("vip.home"))

