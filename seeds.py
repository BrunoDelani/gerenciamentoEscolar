from app import db
from app.models.tables import Aluno, Disciplina, Professor, Professor_disciplina, Etapa, Nota
import bcrypt

# Alunos
# Aluno 1:
senha_plana_aluno_1 = "1234"
senha_encriptada_aluno_1 = bcrypt.hashpw(senha_plana_aluno_1.encode('utf-8'), bcrypt.gensalt())
aluno_1 = Aluno(nome="Bruno Delani Cirino dos Santos", email="br.delani@gmail.com", senha=senha_encriptada_aluno_1)

# Aluno 2:
senha_plana_aluno_2 = "4321"
senha_encriptada_aluno_2 = bcrypt.hashpw(senha_plana_aluno_2.encode('utf-8'), bcrypt.gensalt())
aluno_2 = Aluno(nome="Pedro Luís Ferronato Barreto", email="pedroluisfbar@gmail.com", senha=senha_encriptada_aluno_2)

# Aluno 3:
senha_plana_aluno_3 = "123"
senha_encriptada_aluno_3 = bcrypt.hashpw(senha_plana_aluno_3.encode('utf-8'), bcrypt.gensalt())
aluno_3 = Aluno(nome="João Vitor Lopes Alves", email="jvlaaa@gmail.com", senha=senha_encriptada_aluno_3)

db.session.add(aluno_1)
db.session.add(aluno_2)
db.session.add(aluno_3)
db.session.commit()


# Disciplinas
# Disciplina 1:
disciplina_1 = Disciplina(nome="Matemática", calculo="Ponderada")

# Disciplina 2:
disciplina_2 = Disciplina(nome="Português", calculo="Aritimética")

# Disciplina 3:
disciplina_3 = Disciplina(nome="Informática", calculo="Ponderada")

db.session.add(disciplina_1)
db.session.add(disciplina_2)
db.session.add(disciplina_3)
db.session.commit()

# Professor
# Professor 1:
senha_plana_professor_1 = "professor1"
senha_encriptada_professor_1 = bcrypt.hashpw(senha_plana_professor_1.encode('utf-8'), bcrypt.gensalt())
professor_1 = Professor(nome="Fabiano Pescador", email="fabianopescador@gmail.com", senha=senha_encriptada_professor_1)

# Professor 2:
senha_plana_professor_2 = "professor2"
senha_encriptada_professor_2 = bcrypt.hashpw(senha_plana_professor_2.encode('utf-8'), bcrypt.gensalt())
professor_2 = Professor(nome="Lucas Oliveira", email="lucasoliveira@gmail.com", senha=senha_encriptada_professor_2)

#Professor 3:
senha_plana_professor_3 = "professor3"
senha_encriptada_professor_3 = bcrypt.hashpw(senha_plana_professor_3.encode('utf-8'), bcrypt.gensalt())
professor_3 = Professor(nome="Tays Rutti", email="taysrutti@gmail.com", senha=senha_encriptada_professor_3)

#Professor 4:
senha_plana_professor_4 = "professor4"
senha_encriptada_professor_4 = bcrypt.hashpw(senha_plana_professor_4.encode('utf-8'), bcrypt.gensalt())
professor_4 = Professor(nome="Diogo Cléber", email="dcifro@gmail.com", senha=senha_encriptada_professor_4)


db.session.add(professor_1)
db.session.add(professor_2)
db.session.add(professor_3)
db.session.add(professor_4)
db.session.commit()

# Professor_Disciplinas
# Professor_Disciplina 1:
professor_disciplina_1 = Professor_disciplina(professor_id=1, disciplina_id=1)

# Professor_Disciplina 2:
professor_disciplina_2 = Professor_disciplina(professor_id=2, disciplina_id=2)

# Professor_Disciplina 3:
professor_disciplina_3 = Professor_disciplina(professor_id=3, disciplina_id=3)

db.session.add(professor_disciplina_1)
db.session.add(professor_disciplina_2)
db.session.add(professor_disciplina_3)
db.session.commit()

# Etapa
# Etapa 1 Disciplina 1:
etapa_1_disciplina_1 = Etapa(disciplina_id=1, descricao="Prova")

#Etapa 2 Disciplina 1:
etapa_2_disciplina_1 = Etapa(disciplina_id=1, descricao="Trabalho_1")

#Etapa 3 Disciplina 1:
etapa_3_disciplina_1 = Etapa(disciplina_id=1, descricao="Trabalho_2")

# Etapa 1 Disciplina 2:
etapa_1_disciplina_2 = Etapa(disciplina_id=2, descricao="Prova")

#Etapa 2 Disciplina 2:
etapa_2_disciplina_2 = Etapa(disciplina_id=2, descricao="Trabalho_1")

#Etapa 3 Disciplina 2:
etapa_3_disciplina_2 = Etapa(disciplina_id=2, descricao="Trabalho_2")

# Etapa 1 Disciplina 3:
etapa_1_disciplina_3 = Etapa(disciplina_id=3, descricao="Prova")

#Etapa 2 Disciplina 3:
etapa_2_disciplina_3 = Etapa(disciplina_id=3, descricao="Trabalho_1")

#Etapa 3 Disciplina 3:
etapa_3_disciplina_3 = Etapa(disciplina_id=3, descricao="Trabalho_2")

db.session.add(etapa_1_disciplina_1)
db.session.add(etapa_2_disciplina_1)
db.session.add(etapa_3_disciplina_1)
db.session.add(etapa_1_disciplina_2)
db.session.add(etapa_2_disciplina_2)
db.session.add(etapa_3_disciplina_2)
db.session.add(etapa_1_disciplina_3)
db.session.add(etapa_2_disciplina_3)
db.session.add(etapa_3_disciplina_3)
db.session.commit()

# Nota
# Nota 1:
nota_1_aluno_1_etapa_1 = Nota(aluno_id=1, etapa_id=1, nota=60)
nota_2_aluno_1_etapa_2 = Nota(aluno_id=1, etapa_id=2, nota=80)
nota_3_aluno_1_etapa_3 = Nota(aluno_id=1, etapa_id=3, nota=100)

db.session.add(nota_1_aluno_1_etapa_1)
db.session.add(nota_2_aluno_1_etapa_2)
db.session.add(nota_3_aluno_1_etapa_3)
db.session.commit()

