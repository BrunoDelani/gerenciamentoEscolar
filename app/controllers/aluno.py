from app import app
from flask import render_template, redirect, url_for, request
from app.models.tables import Aluno
from app import db
import bcrypt

@app.route('/alunos')
def listar_alunos():
    msg = request.args.get('msg')
    alunos = Aluno.query.all()
    return render_template("listar_aluno.html", lista=alunos, msg=msg)

@app.route('/alunos/deletar/<aluno_id>')
def deletar_aluno(aluno_id):
    select_aluno = Aluno.query.filter_by(id=aluno_id).first()
    db.session.delete(select_aluno)
    db.session.commit()
    return redirect(url_for('listar_alunos', msg='deletado'))

@app.route('/alunos/alterar/<aluno_id>', methods=['GET', 'POST'])
def alterar_aluno(aluno_id):
    if request.method == 'GET':
        select_aluno = Aluno.query.filter_by(id=aluno_id).first()
        return render_template('aluno_formulario.html', aluno=select_aluno, tipo='alterar')
    elif request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']

        alter_aluno = Aluno.query.filter_by(id=aluno_id).first()
        alter_aluno.nome = nome
        alter_aluno.email = email

        db.session.add(alter_aluno)
        db.session.commit()
        return redirect(url_for('listar_alunos', msg='alterado'))

@app.route('/alunos/inserir', methods=['GET', 'POST'])
def inserir_aluno():
    if request.method == 'GET':
        return render_template('aluno_formulario.html', tipo='inserir')

    elif request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha_plana = request.form['senha']
        senha = bcrypt.hashpw(senha_plana.encode('utf-8'), bcrypt.gensalt())
        
        insert_aluno = Aluno(nome = nome, email = email, senha = senha)
        db.session.add(insert_aluno)
        db.session.commit()
        return redirect(url_for('listar_alunos', msg='inserir'))

