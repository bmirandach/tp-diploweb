from flask import Flask #importo la clase
from flask import render_template
from flask import g, flash
from flask import abort, request, redirect, url_for
from flask_bootstrap import Bootstrap

from Post import Post
from FormCreate import FormCreate

post1 = Post(1, 'Titulo 1', 'Aliquam viverra dolor ex, in pulvinar justo efficitur vitae. Pellentesque augue elit, dapibus id quam sit amet, suscipit mattis justo. Quisque fermentum vel dui sed efficitur. Vivamus dapibus imperdiet fringilla. Curabitur venenatis, ex elementum interdum elementum, diam magna facilisis risus.')
post2 = Post(2, 'Titulo 2', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent est nulla, sollicitudin nec tellus sit amet, scelerisque facilisis augue. Donec interdum nunc id venenatis consequat. Donec viverra molestie eros, et luctus arcu imperdiet at. Proin.')
post3 = Post(3, 'Titulo 3', 'Etiam nec vestibulum lacus. Nulla facilisi. Etiam at lorem eget risus gravida feugiat. Mauris pulvinar ligula nisi, eget scelerisque sapien facilisis eu. Vestibulum quis nunc id leo dignissim rutrum. Suspendisse vitae lacus turpis. In egestas blandit nulla. Praesent id dolor venenatis, porta urna.')
post4 = Post(4, 'Titulo 4', 'Etiam nec vestibulum lacus. Nulla facilisi. Etiam at lorem eget risus gravida feugiat. Mauris pulvinar ligula nisi, eget scelerisque sapien facilisis eu. Vestibulum quis nunc id leo dignissim rutrum. Suspendisse vitae lacus turpis. In egestas blandit nulla. Praesent id dolor venenatis, porta urna.')
post5 = Post(5, 'Titulo 5', 'Etiam nec vestibulum lacus. Nulla facilisi. Etiam at lorem eget risus gravida feugiat. Mauris pulvinar ligula nisi, eget scelerisque sapien facilisis eu. Vestibulum quis nunc id leo dignissim rutrum. Suspendisse vitae lacus turpis. In egestas blandit nulla. Praesent id dolor venenatis, porta urna.')
post6 = Post(6, 'Titulo 6', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent orci dui, ultricies ut felis id, cursus venenatis nibh. Duis hendrerit neque sed consectetur faucibus. Etiam consequat risus elit, non scelerisque nisl facilisis ut. Aenean ultricies quam et.')
post7 = Post(7, 'Titulo 7', 'Etiam nec vestibulum lacus. Nulla facilisi. Etiam at lorem eget risus gravida feugiat. Mauris pulvinar ligula nisi, eget scelerisque sapien facilisis eu. Vestibulum quis nunc id leo dignissim rutrum. Suspendisse vitae lacus turpis. In egestas blandit nulla. Praesent id dolor venenatis, porta urna.')
post8 = Post(8, 'Titulo 8', 'Etiam nec vestibulum lacus. Nulla facilisi. Etiam at lorem eget risus gravida feugiat. Mauris pulvinar ligula nisi, eget scelerisque sapien facilisis eu. Vestibulum quis nunc id leo dignissim rutrum. Suspendisse vitae lacus turpis. In egestas blandit nulla. Praesent id dolor venenatis, porta urna.')
list_p = [post1, post2, post3, post4, post5, post6, post7, post8]

app=Flask(__name__) #inicializar la app
app.config['SECRET_KEY'] = 'xxDDF878945f7f8t9gWavp5p' # MUY necesaria para flask-wtf

bootstrap = Bootstrap(app)

@app.before_request
def get_posts():
    g.list_posts = list_p

@app.route('/agregar', methods=['GET', 'POST'])
def create():
    create = FormCreate()
    if request.method == 'POST':
        if create.validate_on_submit():
            #details=request.form
            #print(details["Título"])
            #print(details["Descripción"])
            newPost = Post(len(g.list_posts)+1, create.titlePost.data, create.contentPost.data)
            #newPost = Post(len(g.list_posts)+1, details["Título"], details["Descripción"])
            g.list_posts.append(newPost)
            flash(f"El Post {newPost.getPost_id()} se creo con exito")
            return redirect(url_for('content', post_id=newPost.getPost_id()))
        else:
            flash("Error. Revise los datos del formulario.")
            #print('no pasa')
    return render_template('create.html', form=create)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contacto')
def contact():
    return render_template("contact.html")


@app.route('/contenidos')
def contents():
    return render_template("contents.html", list_posts=g.list_posts)

@app.route('/contenido/<post_id>')
def content(post_id):
    the_post = next((post for post in g.list_posts if post.post_id == int(post_id)), None)
    if not the_post:
        return abort(404)
    return render_template("content.html", post=the_post)



if __name__ == '__main__': # Comprobamos que, si estamos en el archivo principal (main), entonces ejecutamos la aplicación
    app.run(debug=True)

