from flask import Blueprint, render_template

# Create a blueprint for authentication routes
auth_bp = Blueprint('auth', __name__, template_folder='templates')

# Define authentication routes
@auth_bp.route('/login')
def login():
    return render_template('auth/login.html')

@auth_bp.route('/signup')
def signup():
    return render_template('auth/signup.html')

# Add more routes as needed
