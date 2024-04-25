from flask import Blueprint

researcher_bp = Blueprint('researcher', __name__, template_folder='templates', static_folder='static')

from app.researcher import routes
