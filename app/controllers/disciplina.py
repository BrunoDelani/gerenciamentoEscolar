from app import app
from flask import render_template, redirect, url_for, request
from app.models.tables import Disciplina
from app import db
import bcrypt

@app.route('/disciplinas')
def listar_disciplinas():
    msg = request.args.get('msg')
    disciplinas = Disciplina.query.all()
    return render_template("listar_disciplina.html", lista=disciplinas, msg=msg)

@app.route('/disciplinas/deletar/<disciplina_id>')
def deletar_disciplina(disciplina_id):
    select_disciplina = Disciplina.query.filter_by(id=disciplina_id).first()
    db.session.delete(select_disciplina)
    db.session.commit()
    return redirect(url_for('listar_disciplinas', msg='deletado'))

@app.route('/disciplinas/alterar/<disciplina_id>', methods=['GET', 'POST'])
def alterar_disciplina(disciplina_id):
    if request.method == 'GET':
        select_disciplina = Disciplina.query.filter_by(id=disciplina_id).first()
        return render_template('disciplina_formulario.html', disciplina=select_disciplina, tipo='alterar')
    elif request.method == 'POST':
        nome = request.form['nome']
        calculo = request.form['calculo']

        alter_disciplina = Disciplina.query.filter_by(id=disciplina_id).first()
        alter_disciplina.nome = nome
        alter_disciplina.calculo = calculo

        db.session.add(alter_disciplina)
        db.session.commit()
        return redirect(url_for('listar_disciplinas', msg='alterado'))

@app.route('/disciplinas/inserir', methods=['GET', 'POST'])
def inserir_disciplina():
    if request.method == 'GET':
        return render_template('disciplina_formulario.html', tipo='inserir')

    elif request.method == 'POST':
        nome = request.form['nome']
        calculo = request.form['calculo']
        
        insert_disciplina = Disciplina(nome = nome, calculo = calculo)
        db.session.add(insert_disciplina)
        db.session.commit()
        return redirect(url_for('listar_disciplinas', msg='inserir'))

