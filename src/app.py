import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Soporte para PostgreSQL en Render y SQLite en local
    db_url = os.environ.get('DATABASE_URL', 'sqlite:///estudiantes.db')
    if db_url.startswith("postgres://"):
          db_url = db_url.replace("postgres://", "postgresql+psycopg://", 1)
        
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from src.models import bd
    bd.init_app(app)

    with app.app_context():
        bd.create_all()

    from src.routes import estudiantes_bp
    app.register_blueprint(estudiantes_bp)

    return app
