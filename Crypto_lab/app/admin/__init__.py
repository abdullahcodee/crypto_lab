from flask import Blueprint

admin_templates_bp = Blueprint('admin_templates', __name__, template_folder='admin')

from app.admin import routes
