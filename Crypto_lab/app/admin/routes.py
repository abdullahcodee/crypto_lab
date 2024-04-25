from flask import render_template, Blueprint

admin_bp = Blueprint('admin', __name__, template_folder='templates')

@admin_bp.route('/admin')
def index():
    return render_template('admin/index.html')

@admin_bp.route('/admin/user_verification')
def user_verification():
    return render_template('admin/user_verification.html')

@admin_bp.route('/admin/user_management')
def user_management():
    return render_template('admin/user_management.html')

@admin_bp.route('/admin/package_management')
def package_management():
    return render_template('admin/package_management.html')
