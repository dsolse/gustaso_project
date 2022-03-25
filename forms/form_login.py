from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import PasswordField, StringField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

from models.guapos import Guapos


class LoginForm(FlaskForm):	
	apellido = StringField("apellido del guapo", validators=[InputRequired(), Length(min=3, max=20)], render_kw={"placeholder" : "Escribe el apellido del guapo"})	

	password = PasswordField("Escribe password", validators=[InputRequired(), Length(min=2, max=10)])

	submit = SubmitField("Enviar")

