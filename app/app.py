from flask import Flask #importo la clase
from flask import render_template

app=Flask(__name__) #inicializar la app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contenidos')
def contents():
    return render_template("contents.html")

@app.route('/contenido')
def content():
    return render_template("content.html")


if __name__ == '__main__': # Comprobamos que, si estamos en el archivo principal (main), entonces ejecutamos la aplicación
    app.run(debug=True)

