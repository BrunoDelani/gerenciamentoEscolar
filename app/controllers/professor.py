from app import app
from flask import render_template, redirect, url_for, request
from app.models.tables import Professor
from app import db
import bcrypt

from flask_login import login_required

@app.route('/professores')
@app.route('/professores/pagina/<int:pagina>/')
@login_required
def listar_professores(pagina = 1):
    msg = request.args.get('msg')
    nome = request.args.get('nome')
    if nome:
        nome = '%' + nome + '%'
        paginacao = Professor.query.filter(Professor.nome.like(nome)).paginate(page = pagina, per_page= 10)
        professores = paginacao.items
        total_paginas = paginacao.total
        totalpaginas = total_paginas/10
        totalpaginas = round(totalpaginas + 0.5)
    else:
        # professores = Professor.query.all()
        paginacao = Professor.query.paginate(page = pagina, per_page= 10)
        professores = paginacao.items
        total_paginas = paginacao.total
        totalpaginas = total_paginas/10
        totalpaginas = round(totalpaginas + 0.5)


    return render_template("listar_professores.html", lista=professores, mensagem = msg, paginas = int(totalpaginas), pagina_atual = pagina)


@app.route('/professores/deletar/<professor_id>')
def deletar_professor(professor_id):
    pf = Professor.query.filter_by(id=professor_id).first()
    db.session.delete(pf)
    db.session.commit()
    return redirect(url_for('listar_professores', msg='deletado'))


@app.route('/professores/alterar/<professor_id>', methods=['GET', 'POST'])
def alterar_professor(professor_id):
    if request.method == 'GET':
        pf = Professor.query.filter_by(id=professor_id).first()
        return render_template('professor_formulario.html', professor=pf, tipo='alterar')
    elif request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']

        prof = Professor.query.filter_by(id=professor_id).first()
        prof.nome = nome
        prof.email = email

        db.session.add(prof)
        db.session.commit()
        return redirect(url_for('listar_professores', msg='alterado'))

@app.route('/professores/inserir', methods=['GET', 'POST'])
def inserir_professor():
    if request.method == 'GET':
        return render_template('professor_formulario.html', tipo='inserir')

    elif request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha_plana = request.form['senha']
        senha = bcrypt.hashpw(senha_plana.encode('utf-8'), bcrypt.gensalt())
        
        professor = Professor(nome = nome, email = email, senha = senha)
        db.session.add(professor)
        db.session.commit()
        return redirect(url_for('listar_professores', msg='inserir'))
