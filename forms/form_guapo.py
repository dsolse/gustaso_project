from flask_wtf import FlaskForm
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import PasswordField, StringField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

class GuapuraForm(FlaskForm):
    apellido = StringField(
        "apellido del guapo",
        validators=[InputRequired(), Length(min=3, max=20)],
        render_kw={"placeholder": "Escribe el apellido del guapo"},
    )

    guapura = IntegerField("Type guapura", validators=[InputRequired()])


    submit = SubmitField("Enviar")

    def validate_guapura(self, guapura):
        if guapura.data < 0 or guapura.data > 10:
            raise ValidationError("GUapura es del 1 al 10")
