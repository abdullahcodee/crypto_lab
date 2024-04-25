from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class UserVerificationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    verify = SubmitField('Verify')

class UserManagementForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    add_user = SubmitField('Add User')
    remove_user = SubmitField('Remove User')

class PackageManagementForm(FlaskForm):
    package_name = StringField('Package Name', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    add_package = SubmitField('Add Package')
    remove_package = SubmitField('Remove Package')
