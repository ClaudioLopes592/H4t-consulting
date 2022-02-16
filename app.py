from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sobre-nos')
def sobre():
    return render_template('sobre.html')


@app.route('/quem-somos')
def somos():
    return render_template('quem-somos.html')


@app.route('/fazemos')
def fazemos():
    return render_template('fazemos.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/o-cliente-interno')
def cliente():
    return render_template('o-cliente-interno.html')


@app.route('/gestao-pessoas')
def gestao():
    return render_template('gestao-pessoas.html')


@app.route('/magia')
def magia():
    return render_template('magia.html')


@app.route('/lado-sombra')
def sombra():
    return render_template('lado-sombra.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


if __name__ == '__main__':
    app.run(debug=True)
