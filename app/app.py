import os
from flask import Flask #importo la clase
from flask import render_template, flash
from flask import abort, request, redirect, url_for
from flask_bootstrap import Bootstrap
from datetime import datetime #para el post
from werkzeug.security import generate_password_hash, check_password_hash #para contraseñas
from flask_login import LoginManager
from flask_login import UserMixin
from flask_login import current_user, login_user, logout_user, login_required

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from FormUser import UserCreate, LoginForm
from FormPost import PostCreate, PostUpdate, FavoriteForm

projectdir = os.path.abspath(os.path.join(os.path.dirname(__file__),"..")) #donde esta app 
db_path = os.path.join(projectdir, 'blog.db')

app=Flask(__name__) #inicializar la app
app.config['SECRET_KEY'] = 'xxDDF878945f7f8t9gWavp5p'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
login = LoginManager(app)
login.login_view = 'login' #indica que la funcion login es la que se encarga de los inicios de sesion
login.login_message = 'Inicia sesión para ver esta página'

Favorites = db.Table(
    'favorites',
    db.Column('user_id', db.Integer, db.ForeignKey('Users.id'), primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('Posts.id'), primary_key=True)
)


class User(UserMixin, db.Model):
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

    def like(self, post):
        if not self.is_favorite(post):
            self.likes.append(post)

    def dislike(self, post):
        if self.is_favorite(post):
            self.likes.remove(post)

    def is_favorite(self, post):
        return self.likes.filter(
            Favorites.c.post_id == post.id).count() > 0

    def favorite_posts(self):
        return Post.query.join(
            Favorites, (Favorites.c.post_id == Post.id)).filter(
                Favorites.c.user_id == self.id).order_by(
                    Post.timestamp.desc())


class Post(db.Model):
    __tablename__ = 'Posts'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(64), nullable=False)
    subtitle = db.Column(db.String(120), nullable=True)
    content = db.Column(db.Text, nullable=False)
    image_link = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.Date(), index=True, default=datetime.utcnow)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/agregar', methods=['GET', 'POST'])
def create():
    form = PostCreate()
    if request.method == 'POST':
        if create.validate_on_submit():
            post = Post(title=form.title.data, subtitle=form.subtitle.data,
                        content=form.content.data, image_link=form.image.data)
            db.session.add(post)
            db.session.commit()
            flash(f'El post {post.id} se creo con exito')
            return redirect(url_for('content', post_id=post.id))
        else:
            flash('Error. Revise los datos del formulario.')
    return render_template('create.html', form=form)

@app.route('/modificar/<post_id>', methods=['GET','POST'])
def update(post_id):
    update = PostUpdate()
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        if update.validate_on_submit():
            post.title = update.title.data
            post.subtitle = update.subtitle.data
            post.content = update.content.data
            post.image_link = update.image.data
            db.session.add(post)
            db.session.commit()
            flash(f'El Post {post.id} se modifico con exito')
            return redirect(url_for('content', post_id=post_id))
    #entra al formulario, GET
    return render_template('update.html', form=update, post=post)

@app.route('/eliminar/<post_id>')
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash(f'El Post {post_id} se elimino con exito')
    return redirect(url_for('contents'))

@app.route('/crear-usuario', methods=['GET', 'POST'])
def create_user():
    create = UserCreate()
    if request.method == 'POST':
        if create.validate_on_submit():
            newUser = User(username=create.username.data, password=create.password.data, email=create.email.data)
            newUser.set_password(create.password.data)
            db.session.add(newUser)
            db.session.commit()
            flash(f'Su usuario {newUser.username} se creó con éxito')
            #no lo lleva a su perfil, lo lleva al login para que inicie su sesion
            #return redirect(url_for('profile', user_id=newUser.id))
            return redirect(url_for('login'))
        else:
            flash('Error. Revise los datos del formulario.')
    return render_template('signin.html', form=create)

@app.route('/iniciar-sesion', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        print(form.username.data)
        print(user.password)
        print(form.password.data)
        if user is None or not user.check_password(form.password.data):
            flash('Usuario o contraseña invalida')
            return redirect(url_for('login'))
        #si password y user son correctos la funcion registra al usuario como logueado
        login_user(user)
        flash(f'Iniciaste sesión con el usuario {form.username.data}')
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/salir')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/')
def index():
    print(db_path)
    all_contents = Post.query.all() #si uso first como traigo los otros 2?
    return render_template('index.html', list_posts=all_contents)

@app.route('/contacto')
def contact():
    return render_template('contact.html')


@app.route('/posts')
def contents():
    all_contents = Post.query.all()
    return render_template('contents.html', list_posts=all_contents)

@app.route('/post/<post_id>')
@login_required
def content(post_id):
    the_post = Post.query.get_or_404(post_id) #ver si redirigir a una pagina de error
    # if not the_post:
    #     return abort(404)
    form = FavoriteForm()
    return render_template('content.html', post=the_post, form=form)


@app.route('/favorito/<post_id>', methods=['POST'])
@login_required
def like(post_id):
    form = FavoriteForm()
    if form.validate_on_submit():
        post = Post.query.filter_by(id=post_id).first()
        if post is None:
            flash(f'No se encuentra el post {post_id}')
            return redirect(url_for('index'))
        current_user.like(post)
        db.session.commit()
        flash(f'Agregaste a Favoritos el post {post_id}!')
        return redirect(url_for('content', post_id=post_id))
    else:
        return redirect(url_for('index'))


@app.route('/desfavorito/<post_id>', methods=['POST'])
@login_required
def dislike(post_id):
    form = FavoriteForm()
    if form.validate_on_submit():
        post = Post.query.filter_by(id=post_id).first()
        if post is None:
            flash(f'No se encuentra el post {post_id}')
            return redirect(url_for('index'))
        current_user.dislike(post)
        db.session.commit()
        flash(f'Sacaste de Favoritos el post {post_id}!')
        return redirect(url_for('content', post_id=post_id))
    else:
        return redirect(url_for('index'))

@app.route('/perfil/<user_id>')
@login_required
def profile(user_id):
    user = User.query.get_or_404(user_id)
    # aca busca todos los posts que este usuario tenga marcados como favoritos y se los pasa al template
    favorite_posts = current_user.favorite_posts().all()
    return render_template('profile.html', user=user, list_posts=favorite_posts)

@app.route('/usuarios')
@login_required
def users():
    all_users = User.query.all()
    return render_template('users.html', list_users=all_users)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

if __name__ == '__main__': 
    app.run(debug=True)

