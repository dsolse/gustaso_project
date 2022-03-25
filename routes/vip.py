from flask import Blueprint
from flask.templating import render_template
from flask_login import current_user
from flask_login.utils import login_required
from models.guapos import Guapos

vip = Blueprint("vip", __name__, url_prefix="/vip")


@vip.route("/")
@login_required
def home():
	return render_template("vip.html", user=current_user)

@vip.route("/guapos")
@login_required
def guapos():
	return render_template("home.html", user=current_user, rows=Guapos.query.all())
