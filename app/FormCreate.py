from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class FormCreate(FlaskForm):
    titlePost = StringField("Título", validators=[DataRequired()])
    contentPost = StringField("Descripción", validators=[DataRequired()])
    submit = SubmitField("Subir")