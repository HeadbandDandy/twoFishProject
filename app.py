from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
import os




# Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '\x14B~^\x07\xe1\x197\xda\x18\xa6[[\x05\x03QVg\xce%\xb2<\x80\xa4\x00'
app.config['DEBUG'] = True

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
db = SQLAlchemy(app)

# database models set up below
class Todos(db.Model):
     _id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String(200) , nullable=False)
     description = db.Column(db.String(500), nullablle=False)
     created_at = db.Column(db.DateTime, default= datetime.utcnow)
     

# db.create_all()



@app.route("/")
def home():
    
    return render_template('index.html')



if __name__ == "__main__":
    app.run(port=3000)




