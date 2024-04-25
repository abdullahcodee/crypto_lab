from flask_wtf import FlaskForm
from wtforms import TextAreaField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired

class CipherForm(FlaskForm):
    text = TextAreaField('Text', validators=[DataRequired()])
    method = SelectField('Method', choices=[('atbash', 'Atbash Cipher'), ('caesar', 'Caesar Cipher'), ('simple_substitution', 'Simple Substitution')], validators=[DataRequired()])
    key = StringField('Key')
    shift = StringField('Shift')
    action = SelectField('Action', choices=[('encrypt', 'Encrypt'), ('decrypt', 'Decrypt')], validators=[DataRequired()])
    submit = SubmitField('Submit')
