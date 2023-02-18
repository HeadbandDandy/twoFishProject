from flask import Flask
from app.routes import home
from app.db import init_db
# from app.utils import filters


def create_app(test_config=None):
    # Flask
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        SECRET_KEY='super_secret_key'
    )
    
    
    
    # render template here
    @app.route('/hello')
    def hello():
    
        return 'hello world'
    
    # register routes here
    app.register_blueprint(home)
    
    
    init_db()
    
    
    return app 
    
    
    # app.jinja_env.filters['format_url'] = filters.format_url
    # app.jinja_env.filters['format_date'] = filters.format_date
    # app.jinja_env.filters['format_plural_words'] = filters.format_plural_words

  

















