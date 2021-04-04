from app import db
from flask_login import UserMixin

class Aluno(db.Model):
    __tablename__ = 'aluno'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), index=True, unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Aluno %s>' % self.nome

class Disciplina(db.Model):
    __tablename__ = 'disciplina'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    calculo = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Disciplina %s>' % self.nome

class Professor(db.Model, UserMixin):
    __tablename__ = 'professor'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), unique=True, index=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<Professor %s>' % self.nome

class Professor_disciplina(db.Model):
    __tablename__ = 'professor_disciplina'

    id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplina.id'), nullable=False)

class Etapa(db.Model):
    __tablename__ = 'etapa'

    id = db.Column(db.Integer, primary_key=True)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplina.id'), nullable=False)
    descricao = db.Column(db.String(200))

class Nota(db.Model):
    __tablename__ = 'nota'

    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    etapa_id = db.Column(db.Integer, db.ForeignKey('etapa.id'), nullable=False)
    nota = db.Column(db.Float, nullable=False)

