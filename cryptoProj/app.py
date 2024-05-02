from flask import Flask, redirect, render_template, request, url_for, flash,session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from werkzeug.security import generate_password_hash, check_password_hash
from pycipher import Caesar, Atbash, SimpleSubstitution, Affine, Autokey, Beaufort, PolybiusSquare, Playfair, Railfence, Rot13, Vigenere


app = Flask(__name__, static_folder='assets', static_url_path='/assets')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cryptolab.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Add a secret key for CSRF protection
db = SQLAlchemy(app)

# Define the database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

class SigninForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

# Use the SigninForm in your sign-in route
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()  # Create an instance of the SigninForm

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            # Successful sign-in
            # Redirect to the dashboard or index page
            return redirect(url_for('dashboard'))
        else:
            # Failed sign-in
            flash('Invalid email or password', 'error')

    # Render the sign-in page along with the form
    return render_template('signin.html', form=form)

from flask import session

@app.route('/logout')
def logout():
    # Clear the user's session data
    session.clear()
    # Redirect the user to the sign-in page
    return redirect(url_for('signin'))


@app.route('/dashboard')
def dashboard():
    # This is just a placeholder for the dashboard route
    return render_template('index.html')


@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if the email is already registered
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            error_message = "Email already registered. Please use a different email."
            flash(error_message, 'error')
            return render_template('signup.html', error=error_message)  # Include error in the template

        # Hash the password before storing it in the database
        hashed_password = generate_password_hash(password)

        # Create a new user instance
        new_user = User(name=name, email=email, password=hashed_password)

        # Add the new user to the database session
        db.session.add(new_user)
        db.session.commit()

        # Redirect to the sign-in page after successful sign-up
        flash('Sign up successful. Please sign in.', 'success')
        return redirect(url_for('signin'))

    # Render the sign-up page for GET requests
    return render_template('signup.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text', '')
        method = request.form.get('method', '')
        key = request.form.get('key', '')
        shift = request.form.get('shift', '')

        # Check if all required fields are filled
        if not text or not method:
            return "Please fill in all required fields: Text and Method"

        if method in ['caesar', 'affine', 'vigenere']:
            if not key and not shift:
                return "Please provide either a Key or a Shift value for the chosen cipher method"

        if method == 'caesar':
            if not shift:
                return "Please provide a Shift value for the Caesar cipher"
            try:
                shift = int(shift)
            except ValueError:
                return "Invalid Shift value. Shift must be an integer."

        if method == 'vigenere':
            if not key:
                return "Please provide a Key for the Vigenere cipher"
            if not key.isalpha():
                return "Invalid Key for Vigenere cipher. Key must contain only alphabetic characters."

        if method == 'affine':
            if not key:
                return "Please provide a Key for the Affine cipher"
            try:
                a, b = map(int, key.split(','))
            except ValueError:
                return "Invalid Key format for Affine cipher. Key must be in the format 'a,b' where a and b are integers."

        if method == 'beaufort':
            if not key:
                return "Please provide a Key for the Beaufort cipher"
            if not key.isalpha():
                return "Invalid Key for Beaufort cipher. Key must contain only alphabetic characters."

        # Perform the encryption/decryption based on the selected method
        if method == 'caesar':
            if request.form['action'] == 'encrypt':
                result = Caesar(shift).encipher(text)
            else:
                result = Caesar(shift).decipher(text)
        elif method == 'atbash':
            if request.form['action'] == 'encrypt':
                result = Atbash().encipher(text)
            else:
                result = Atbash().decipher(text)
        elif method == 'simple_substitution':
            key = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
            if request.form['action'] == 'encrypt':
                result = SimpleSubstitution(key).encipher(text)
            else:
                result = SimpleSubstitution(key).decipher(text)
        elif method == 'affine':
            if request.form['action'] == 'encrypt':
                result = Affine(a, b).encipher(text)
            else:
                result = Affine(a, b).decipher(text)

        elif method == 'autokey':
            if request.form['action'] == 'encrypt':
                result = Autokey(key).encipher(text)
            else:
                result = Autokey(key).decipher(text)
        elif method == 'beaufort':
            if request.form['action'] == 'encrypt':
                result = Beaufort(key).encipher(text)
            else:
                result = Beaufort(key).decipher(text)
        elif method == 'polybius_square':
            if request.form['action'] == 'encrypt':
                if len(key) != 25 and len(key) != 36:
                    return "Invalid key for Polybius Square cipher. Key must have a length of 25 (for a 5x5 square) or 36 (for a 6x6 square)."
                result = PolybiusSquare(key).encipher(text)

            else:
                if len(key) != 25 and len(key) != 36:
                    return "Invalid key for Polybius Square cipher. Key must have a length of 25 (for a 5x5 square) or 36 (for a 6x6 square)."
                result = PolybiusSquare(key).decipher(text)
        elif method == 'playfair':
            if request.form['action'] == 'encrypt':
                result = Playfair(key).encipher(text)
            else:
                result = Playfair(key).decipher(text)
        elif method == 'rail_fence':
            if request.form['action'] == 'encrypt':
                result = Railfence(key).encipher(text)
            else:
                result = Railfence(key).decipher(text)
        elif method == 'rot13':
            if request.form['action'] == 'encrypt':
                result = Rot13().encipher(text)
            else:
                result = Rot13().decipher(text)
        elif method == 'vigenere':
            if request.form['action'] == 'encrypt':
                result = Vigenere(key).encipher(text)
            else:
                result = Vigenere(key).decipher(text)
    
        else:
            result = "Invalid method"

        return result

    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
