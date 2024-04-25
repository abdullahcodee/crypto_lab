from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config



# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # Initialize Flask application
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database and migration engine
    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register blueprints
    from app.admin.routes import admin_bp
    from app.auth.routes import auth_bp
    from app.cipher.routes import cipher_bp
    from app.researcher.routes import researcher_bp


    app.register_blueprint(admin_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(cipher_bp)
    app.register_blueprint(researcher_bp)


    # Import models (optional)
    from app.admin import models as admin_models
    from app.auth import models as auth_models
    from app.cipher import models as cipher_models
    from app.researcher import models as researcher_models

    # Ensure that database tables are created (optional)
    with app.app_context():
        db.create_all()

    # Import other necessary modules or configurations here

    return app
