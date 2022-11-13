from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class PostCreate(FlaskForm):
    title = StringField("Título", validators=[DataRequired()])
    subtitle = StringField("Subtítulo", validators=[DataRequired()])
    content = TextAreaField("Descripción", validators=[DataRequired()])
    image =StringField("Link de la imagen", validators=[Optional(), URL()])
    submit = SubmitField("Subir post")

class PostUpdate(FlaskForm):
    title = StringField("Título", validators=[DataRequired()])
    subtitle = StringField("Subtítulo", validators=[DataRequired()])
    content = TextAreaField("Descripción", validators=[DataRequired()])
    image =StringField("Link de la imagen", validators=[Optional(), URL()])
    submit = SubmitField("Guardar post")

# para los favoritos
class FavoriteForm(FlaskForm):
    submit = SubmitField('Submit')