from flask import Blueprint, render_template
from app.models import ToDo
from app.db import get_db

bp = Blueprint('home', __name__, url_prefix='/')

# route for main page
@bp.route('/')
def index():
    # get all todos
    db = get_db()
    todos = db.query(ToDo).order_by(ToDo.created_at.desc()).all()
    return render_template('index.html')

# route for login page
@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/register')
def register():
    return render_template('register.html')