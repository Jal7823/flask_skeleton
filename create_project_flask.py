import os
import subprocess as sub

#name of project
name_project = input('Project Name?\n')

#original path
original_path = '/home/jal/Documentos/py/flask_projets' 
os.chdir(original_path)

#change to path of project
os.mkdir(name_project)
path_project = f'{original_path}/{name_project}'
os.chdir(path_project)

#creation virtualenv environment
sub.run(['virtualenv','env'])

#creation of folder sources
src= 'src'
os.mkdir(src)

#change to path sources and create folder and files
path_src = f'{original_path}/{name_project}/{src}'
os.chdir(path_src)


# list of folders
folders = ['models','routes','templates','utils','static']
folders_statics = ['js','img','css','libs']

#creation of folders in src
for i in folders:
    os.mkdir(i)
    print(f'<== {i} was created successfully ==>')

index = open(f'{path_src}/index.py','w')
index.write(
    """
from flask import Flask
from app import app

with app.context():
    db.create_table()

if __name__ == '__main__':
    app.run(debug=True)
    """
)
index.close()

app = open(f'{path_src}/app.py','w')
app.write(
"""
#External libraries
import os
from flask import Flask,request,jsonify
from flask_restx import Resource,Api,fields,Namespace
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_login import LoginManager

#Internal files
from utils.db import db

app = Flask(__name__)
migrate = Migrate(app,db)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{os.getenv("DB_USER")}:{os.getenv("DB_PASS")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_DATABASE")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

#db = SQLAlchemy(app)
#db.init_app(app)

login_manager.init_app(app)
app.secret_key = 'SUPER SECRET'

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}


api = Api(app,
    title='',
    description='',
    version='0.1.0',
    authorizations=authorizations,
    security='Bearer Auth'
)

@login_manager.user_loader
def load_user(id):
    return Users.query.get(id)


""")
app.close()
#creation of folders in static
path_static = f'{original_path}/{name_project}/{src}/static'
os.chdir(path_static)

for i in folders_statics:
    os.mkdir(i)
    print(f'<== {i} was created successfully in static folder ==>')

#creation and configuration of db
path_utils = f'{original_path}/{name_project}/{src}/utils'
os.chdir(path_utils)
db_file = open('db.py', 'w')
db_file.write(
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""
)
db_file.close()
    #password manager file
password_manager = open('password_manager.py', 'w')
password_manager.write(
"""
from werkzeug.security import generate_password_hash,check_password_hash

def generate_password(password):
    hash_password = generate_password_hash(password,method='pbkdf2:sha256')
    cut_password = hash_password
    return cut_password

def check_password(hash_password,password):
    check = check_password_hash(hash_password,password)
    return check
"""
)
password_manager.close()

    #marshmallow file
ma_file = open('ma.py','w')
ma_file.write(

"""
from flask_marshmallow import Marshmallow

ma = Marshmallow()

"""

)
ma_file.close()




os.chdir(path_project)
sub.run(['code','.'])
print('<== OPEN PROJECT IN VSCODE ==>')
    







