from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+ os.getenv("DB_USUARIO") + ':' + os.getenv("DB_PASSWORD") + '@' + os.getenv("DB_LOCAL") + '/' + os.getenv("DB_DATABASE") + ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv("SECRET")

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

login_manager = LoginManager(app)
login_manager.init_app(app)

from app.models.tables import Aluno, Disciplina, Professor, Professor_disciplina, Etapa, Nota
from app.controllers import professor
from app.controllers import aluno
from app.controllers import disciplina
from app.controllers import usuario