from flask import render_template, redirect, url_for, flash
from .forms import CipherForm
from .models import CipherResult
from flask import Blueprint

cipher_bp = Blueprint('cipher', __name__)

# Cipher logic functions
def atbash_cipher(text):
    return text[::-1]

def caesar_cipher(text, shift):
    cipher_text = ''
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a')) if char.islower() else chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            cipher_text += shifted_char
        else:
            cipher_text += char
    return cipher_text

# Routes
@cipher_bp.route('/cipher', methods=['GET', 'POST'])
def home():
    form = CipherForm()
    if form.validate_on_submit():
        # Perform cipher operations and save result to database
        original_text = form.text.data
        method = form.method.data
        action = form.action.data
        
        if method == 'atbash':
            cipher_text = atbash_cipher(original_text)
        elif method == 'caesar':
            shift = form.shift.data
            cipher_text = caesar_cipher(original_text, shift)
        # Add more cipher methods here
        
        # Save result to database
        result = CipherResult(original_text=original_text, cipher_text=cipher_text, method=method, action=action)
        cipher_bp.session.add(result)
        cipher_bp.session.commit()
        
        flash('Cipher operation completed successfully.', 'success')
        return redirect(url_for('cipher.home'))
    return render_template('cipher/home.html', form=form)

@cipher_bp.route('/result')
def result():
    results = CipherResult.query.all()
    return render_template('cipher/result.html', results=results)
