from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo

class CadastroForm(FlaskForm):
    usuario = StringField("Usuario", validators= [DataRequired()])
    email = StringField("Email", validators= [DataRequired(),Email()])
    password = PasswordField("Senha",[DataRequired()])
    submit = SubmitField('Cadastrar')


class LoginForm(FlaskForm):
    email= StringField("Email", validators= [DataRequired(),Email()])
    senha= PasswordField("Senha",[DataRequired(),EqualTo('confirm',message='Senhas diferentes')])
    remember_me= BooleanField('Lembrar_senha')
    submit = SubmitField('Login')

