from flask import Blueprint, render_template
from app.models import ToDo
from app.db import get_db

bp = Blueprint('home', __name__, url_prefix='/')

# route for main page
@bp.route('/homepage')
def index():
    # get all todos
    db = get_db()
    todos = db.query(ToDo).order_by(ToDo.created_at.desc()).all()
    return render_template('homepage.html')

# route for login page
@bp.route('/')
def signin():
    return render_template('signin.html')
# route for signing up below
@bp.route('/signup')
def signup():
    return render_template('signup.html')


    