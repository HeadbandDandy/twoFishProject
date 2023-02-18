from flask import Blueprint, render_template

bp = Blueprint('home', __name__, url_prefix='/')

# route for main page
@bp.route('/')
def index():
    return render_template('index.html')

# route for login page
@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/register')
def register():
    return render_template('reigster.html')