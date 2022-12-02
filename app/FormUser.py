from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
import email_validator

class UserCreate(FlaskForm):
    name = StringField("Nombre", validators=[DataRequired(), Length(min= 4)])
    surname = StringField("Apellido", validators=[DataRequired(), Length(min= 4)])
    username = StringField("Nombre de usuario", validators=[DataRequired(), Length(min= 5)])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=5)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    imgp =StringField("Foto de perfil (link)", validators=[Optional(), URL()])
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

#Nueva clase para los datos del perfil
# comenté los datos que me parecía que no deberían poder editarse como el nombre, apellido
# (o la contraseña... te olvidaste la contraseña? cuenta nueva)
class UserUpdate(FlaskForm):
    # name = StringField("Nombre", validators=[DataRequired(), Length(min= 4)])
    # surname = StringField("Apellido", validators=[DataRequired(), Length(min= 4)])
    username = StringField("Nombre de usuario", validators=[DataRequired(), Length(min= 5)])
    # password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=5)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    imgp =StringField("Foto de perfil (link)", validators=[Optional(), URL()])
    submit = SubmitField("Guardar perfil")
