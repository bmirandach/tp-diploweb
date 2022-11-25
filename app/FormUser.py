from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
import email_validator

class UserCreate(FlaskForm):
    username = StringField("Nombre de usuario", validators=[DataRequired(), Length(min= 5)])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=5)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Crear usuario")

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar sesión')

class ContactForm(FlaskForm):
    name = StringField("Nombre", validators=[DataRequired(), Length(min= 3)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    message = TextAreaField("Mensaje", validators=[DataRequired(), Length(min=3)])
    submit = SubmitField('Enviar')
