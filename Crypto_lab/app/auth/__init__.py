from flask import Blueprint

auth_templates_bp = Blueprint('auth_templates', __name__, template_folder='auth')

from app.auth import routes
