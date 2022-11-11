from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
import email_validator

class UserCreate(FlaskForm):
    username = StringField("Nombre de usuario", validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Crear")


class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar sesión')
