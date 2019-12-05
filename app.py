from flask import Flask, render_template, request, flash, redirect, url_for
from form import CadastroForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user
 
app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'secret'
db = SQLAlchemy(app)
login_manager = LoginManager(app)

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), unique=True, nullable=True)
    email = db.Column(db.String(12), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.usuario

    
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cadastro', methods=["GET", "POST"])
def Cadastro():
    form = CadastroForm()
    print('passei aqui')
    print(form.validate_on_submit())
    print(form.usuario.data)
    print(form.email.data)
    print(form.password.data)
    if form.validate_on_submit():
        print('passei aqui tambem')
        user = User()
        user.usuario = request.form['usuario']
        user.email = request.form['email']
        user.password = request.form['password']
        db.session.add(user)
        db.session.commit()

    return render_template(
        'cadastro.html',
        form=form
        )


@app.route('/login', methods=["GET", "POST"])
def Login():
    form=LoginForm()
    return render_template(
        'login.html',
         form=form
         )    
@app.route('/materiais', methods=["GET", "POST"])
def Materiais():
    return render_template('materiais.html')
@app.route('/assunto', methods=["GET", "POST"])
def Assunto():
    return render_template('assunto.html')
          

if (__name__ =='__main__'):
    app.run(debug=True, port = 5001)