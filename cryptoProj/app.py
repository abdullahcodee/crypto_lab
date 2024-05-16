from flask import Flask, redirect, render_template, request, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from werkzeug.security import generate_password_hash, check_password_hash
from pycipher import Atbash, Caesar, Railfence, Rot13, Vigenere,Affine

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

@app.route('/caesar')
def caesar():
    return render_template('ceaser.html')

@app.route('/RailFence')
def rail_fence():
    # This is just a placeholder for the Rail Fence cipher route
    return render_template('RailFence.html')

@app.route('/Playfair')
def playfair():
    # This is just a placeholder for the Playfair cipher route
    return render_template('Playfair.html')

@app.route('/Vigenere')
def vigenere():
    # This is just a placeholder for the Vigenere cipher route
    return render_template('Vigenere.html')

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
    result = ""  # Initialize result with an empty string
    if request.method == 'POST':
        text = request.form.get('text', '')
        method = request.form.get('method', '')
        key = request.form.get('key', '')
        shift = request.form.get('shift', '')

        # Check if all required fields are filled
        if not text or not method:
            return "Please fill in all required fields: Text and Method"
            
        elif method == 'atbash':
            if request.form['action'] == 'encrypt':
                words = text.split()  # Split the input text into individual words
                enciphered_words = [Atbash().encipher(word) for word in words]  # Encipher each word separately
                result = ' '.join(enciphered_words)  # Join the enciphered words with a space
            else:
                words = text.split()  # Split the input text into individual words
                deciphered_words = [Atbash().decipher(word) for word in words]  # Decipher each word separately
                result = ' '.join(deciphered_words)  # Join the deciphered words with a space

        elif method == 'rot13':
            if request.form['action'] == 'encrypt':
                words = text.split()  # Split the input text into individual words
                enciphered_words = [Rot13().encipher(word) for word in words]  # Encipher each word separately
                result = ' '.join(enciphered_words)  # Join the enciphered words with a space
            else:
                words = text.split()  # Split the input text into individual words
                deciphered_words = [Rot13().decipher(word) for word in words]  # Decipher each word separately
                result = ' '.join(deciphered_words)  # Join the deciphered words with a space

        elif method == 'vigenere':
            if not key:
                return "Please provide a Key for the Vigenère cipher. Example key: 'KEY'"
            if not key.isalpha():
                return "Invalid Key for Vigenère cipher. Key must contain only alphabetic characters."
            if request.form['action'] == 'encrypt':
                words = text.split()  # Split the input text into individual words
                enciphered_words = [Vigenere(key).encipher(word) for word in words]  # Encipher each word separately
                result = ' '.join(enciphered_words)  # Join the enciphered words with a space
            else:
                words = text.split()  # Split the input text into individual words
                deciphered_words = [Vigenere(key).decipher(word) for word in words]  # Decipher each word separately
                result = ' '.join(deciphered_words)  # Join the deciphered words with a space

        elif method == 'caesar':
            if not shift:
                return "Please provide a Shift value for the Caesar cipher"
            try:
                shift = int(shift)
            except ValueError:
                return "Invalid Shift value. Shift must be an integer."
            if request.form['action'] == 'encrypt':
                words = text.split()  # Split the input text into individual words
                enciphered_words = [Caesar(shift).encipher(word) for word in words]  # Encipher each word separately
                result = ' '.join(enciphered_words)  # Join the enciphered words with a space
            else:
                words = text.split()  # Split the input text into individual words
                deciphered_words = [Caesar(shift).decipher(word) for word in words]  # Decipher each word separately
                result = ' '.join(deciphered_words)  # Join the deciphered words with a space
                
        elif method == 'affine':
            if not key:
                return "Please provide a Key for the Affine cipher"
            try:
                a, b = map(int, key.split(','))
            except ValueError:
                return "Invalid Key format for Affine cipher. Key must be in the format '1,2' where 1 and 2 are integers."
            if request.form['action'] == 'encrypt':
                words = text.split()  # Split the input text into individual words
                enciphered_words = [Affine(a, b).encipher(word) for word in words]  # Encipher each word separately
                result = ' '.join(enciphered_words)  # Join the enciphered words with a space
            else:
                words = text.split()  # Split the input text into individual words
                deciphered_words = [Affine(a, b).decipher(word) for word in words]  # Decipher each word separately
                result = ' '.join(deciphered_words)  # Join the deciphered words with a space

        elif method == 'rail_fence':
            if not key:
                return "Please provide a Key for the Rail Fence cipher. Example key: '3'"
            if not key.isdigit():
                return "Invalid Key for Rail Fence cipher. Key must be a positive integer less than 8 example '3'."

            if request.form['action'] == 'encrypt':
                words = text.split()  # Split the input text into individual words
                enciphered_words = [Railfence(int(key)).encipher(word) for word in words]  # Encipher each word separately
                result = ' '.join(enciphered_words)  # Join the enciphered words with a space
            else:
                words = text.split()  # Split the input text into individual words
                deciphered_words = [Railfence(int(key)).decipher(word) for word in words]  # Decipher each word separately
                result = ' '.join(deciphered_words)  # Join the deciphered words with a space

        else:
            result = "Invalid method"
        return result
    return render_template('index.html')
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
