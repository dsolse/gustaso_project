from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import PasswordField, StringField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

from models.guapos import Guapos


class RegisterForm(FlaskForm):

    name = StringField(
        "Nombre del guapo",
        validators=[InputRequired(), Length(min=3, max=20)],
        render_kw={"placeholder": "Escribe el nombre del guapo"},
    )

    apellido = StringField(
        "apellido del guapo",
        validators=[InputRequired(), Length(min=3, max=20)],
        render_kw={"placeholder": "Escribe el apellido del guapo"},
    )

    soltero = SelectField(
        "Eres soltero", choices=[("1", "Si"), ("2", "No")], validators=[InputRequired()]
    )

    password = PasswordField(
        "Escribe password", validators=[InputRequired(), Length(min=2, max=10)]
    )

    submit = SubmitField("Enviar")

    # validate_ + apellido
    def validate_apellido(self, apellido):
        value_apellido = apellido.data
        user = Guapos.query.filter_by(apellido=value_apellido).first()
        if user:
            raise ValidationError("Necesita ser apellido distinto")
