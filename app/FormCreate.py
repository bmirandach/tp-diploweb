from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class FormCreate(FlaskForm):
    titlePost = StringField("Título *", validators=[DataRequired()])
    subtitlePost = StringField("Subtítulo", validators=[Optional()])
    contentPost = TextAreaField("Descripción *", validators=[DataRequired()])
    imagePost =StringField("Link imagen *", validators=[Optional(), URL()])
    submit = SubmitField("Subir")