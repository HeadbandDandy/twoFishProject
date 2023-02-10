from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# app name below
app = Flask(__name__)
# database configuration below
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# App extension below
db = SQLAlchemy(app)

class User(db.Model):
    pass

class ToDO(db.Model):
    pass
