from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from app.db import init_db 
from app.utils import filters
import os


def create_app(test_config=None):
    # Flask
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '\x14B~^\x07\xe1\x197\xda\x18\xa6[[\x05\x03QVg\xce%\xb2<\x80\xa4\x00'
    app.config['DEBUG'] = True
    
    # render template here
    @app.route("/")
    def home():
    
        return render_template('index.html')


    # Database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True

    app.jinja_env.filters['format_url'] = filters.format_url
    app.jinja_env.filters['format_date'] = filters.format_date
    app.jinja_env.filters['format_plural_words'] = filters.format_plural_words

    init_db(app)

    return app 















