from flask import Blueprint

cipher_bp = Blueprint('cipher', __name__, template_folder='templates')

from . import routes
