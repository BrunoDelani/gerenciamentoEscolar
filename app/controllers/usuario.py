from app import app, db
from app import login_manager
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from app.models.tables import Professor
import bcrypt

@login_manager.user_loader
def get_user(user_id):
    return Professor.query.filter_by(id=user_id).first()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        mensagem = request.args.get('mensagem')
        return render_template("login.html", mensagem = mensagem)

    elif request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        login = Professor.query.filter_by(email=email).first()
        autorizado = False

        if login:
            autorizado = bcrypt.checkpw(senha.encode('utf-8'), login.senha.encode('utf-8'))

        if not login or not autorizado:
            mensagem = "Usuario ou senha inválidos."
            return render_template('login.html', mensagem = mensagem)
        else:
            login_user(login)
            return redirect('/professores')


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')

@login_manager.unauthorized_handler
def nao_autorizado():
    return redirect(url_for('login', mensagem = "Faça login."))