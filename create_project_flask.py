import os
import subprocess as sub
import getpass

# Local imports
from filesFlaskSkeleton import *

# Get username and project name
username = getpass.getuser()
name_project = input('Project Name?\n')

# Set the original path
original_path = f'/home/{username}/Documents/py/flask_projects'
if not os.path.exists(original_path):
    os.makedirs(original_path)

os.chdir(original_path)

# Change to path of project
os.mkdir(name_project)
path_project = f'{original_path}/{name_project}'
os.chdir(path_project)

# Create virtual environment
sub.run(['virtualenv', 'env'])

# Create folder sources
src = 'src'
os.mkdir(src)

# Change to path sources and create folders and files
path_src = f'{original_path}/{name_project}/{src}'
os.chdir(path_src)

# List of folders
folders = ['models', 'routes', 'templates', 'utils', 'static']
folders_statics = ['js', 'img', 'css', 'libs']

# Creation of folders in src
for folder in folders:
    os.mkdir(folder)
    print(f'<== {folder} was created successfully ==>')

# Create index.py
index = open(f'{path_src}/index.py', 'w')
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

# Create app.py
app = open(f'{path_src}/app.py', 'w')
app.write(
"""
# External libraries
import os
from flask import Flask, request, jsonify
from flask_restx import Resource, Api, fields, Namespace
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_login import LoginManager

# Internal files
from utils.db import db

app = Flask(__name__)
migrate = Migrate(app, db)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{os.getenv("DB_USER")}:{os.getenv("DB_PASS")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_DATABASE")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# db = SQLAlchemy(app)
# db.init_app(app)

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
"""
)
app.close()

# Creation of folders in static
path_static = f'{original_path}/{name_project}/{src}/static'
os.chdir(path_static)

for folder in folders_statics:
    os.mkdir(folder)
    print(f'<== {folder} was created successfully in static folder ==>')

# Creation and configuration of db
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

# Password manager file
password_manager = open('password_manager.py', 'w')
password_manager.write(
"""
from werkzeug.security import generate_password_hash, check_password_hash

def generate_password(password):
    hash_password = generate_password_hash(password, method='pbkdf2:sha256')
    return hash_password

def check_password(hash_password, password):
    return check_password_hash(hash_password, password)
"""
)
password_manager.close()

# Marshmallow file
ma_file = open('ma.py', 'w')
ma_file.write(
"""
from flask_marshmallow import Marshmallow

ma = Marshmallow()
"""
)
ma_file.close()

os.chdir(path_project)
sub.run(['code', '.'])
print('<== OPEN PROJECT IN VSCODE ==>')
