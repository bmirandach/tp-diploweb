import os
from flask import Flask #importo la clase
from flask import render_template
from flask import g, flash
from flask import abort, request, redirect, url_for
from flask_bootstrap import Bootstrap
from datetime import datetime #para el post
from werkzeug.security import generate_password_hash, check_password_hash #para contraseñas

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from UserCreate import UserCreate, LoginForm
from FormCreate import FormCreate

projectdir = os.path.abspath(os.path.join(os.path.dirname(__file__),"..")) #donde esta app 
db_path = os.path.join(projectdir, 'blog.db')

app=Flask(__name__) #inicializar la app
app.config['SECRET_KEY'] = 'xxDDF878945f7f8t9gWavp5p'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)

Favorites = db.Table(
    'favorites',
    db.Column('user_id', db.Integer, db.ForeignKey('Users.id'), primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('Posts.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(128))
    admin = db.Column(db.Boolean, default=False)
    likes = db.relationship('Post', secondary=Favorites, backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Post(db.Model):
    __tablename__ = 'Posts'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(64), nullable=False)
    subtitle = db.Column(db.String(120), nullable=True)
    content = db.Column(db.Text, nullable=False)
    image_link = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.Date(), index=True, default=datetime.utcnow)


@app.route('/agregar', methods=['GET', 'POST'])
def create():
    create = FormCreate()
    if request.method == 'POST':
        if create.validate_on_submit():
            newPost = Post(title=create.titlePost.data, subtitle=create.subtitlePost.data, content=create.contentPost.data, image_link=create.imagePost.data)
            db.session.add(newPost)
            db.session.commit()
            flash(f"El Post {newPost.id} se creo con exito")
            return redirect(url_for('content', post_id=newPost.id))
        else:
            flash("Error. Revise los datos del formulario.")
    return render_template('create.html', form=create)

@app.route('/modificar/<post_id>', methods=['GET','POST'])
def update(post_id):
    update = FormCreate()
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        if update.validate_on_submit():
            post.title = update.titlePost.data
            post.subtitle = update.subtitlePost.data
            post.content = update.contentPost.data
            post.image_link = update.imagePost.data
            db.session.add(post)
            db.session.commit()
            flash(f"El Post {post.id} se modifico con exito")
            return redirect(url_for('content', post_id=post_id))
    #entra al formulario, GET
    return render_template('update.html', form=update, post=post)

@app.route('/eliminar/<post_id>')
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash(f"El Post {post_id} se elimino con exito")
    return redirect(url_for('contents'))

@app.route('/crear-usuario', methods=['GET', 'POST'])
def create_user():
    create = UserCreate()
    if request.method == 'POST':
        if create.validate_on_submit():
            newUser = User(username=create.username.data, password=create.password.data, email=create.email.data)
            db.session.add(newUser)
            db.session.commit()
            flash(f"Su usuario {newUser.username} se creo con exito")
            return redirect(url_for('profile', user_id=newUser.id))
        else:
            flash("Error. Revise los datos del formulario.")
    return render_template('createUser.html', form=create)


@app.route('/iniciar-sesion', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Iniciaste sesión con el usuario {}'.format(form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/')
def index():
    print(db_path)
    all_contents = Post.query.all() #si uso first como traigo los otros 2?
    return render_template("index.html", list_posts=all_contents)

@app.route('/contacto')
def contact():
    return render_template("contact.html")


@app.route('/contenidos')
def contents():
    all_contents = Post.query.all()
    return render_template("contents.html", list_posts=all_contents)

@app.route('/contenido/<post_id>')
def content(post_id):
    the_post = Post.query.get_or_404(post_id) #ver si redirigir a una pagina de error
    # if not the_post:
    #     return abort(404)
    return render_template("content.html", post=the_post)

@app.route('/perfil/<user_id>')
def profile(user_id):
    user = User.query.get_or_404(user_id)
    #aca deberia buscar todos los posts que este usuario tenga marcados como favoritos y pasarselos al template
    #mientras... les pasa todos 
    all_contents = Post.query.all()
    return render_template("profile.html", user=user, list_posts=all_contents)

@app.route('/usuarios')
def users():
    all_users = User.query.all()
    return render_template("users.html", list_users=all_users)

if __name__ == '__main__': 
    app.run(debug=True)

