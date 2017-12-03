from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class LogInForm(FlaskForm):
    email_address = StringField("Email Address:", [validators.DataRequired(), validators.Email()])
    password = PasswordField("Password:", [validators.DataRequired()])


class SignUpForm(FlaskForm):
    email_address = StringField("Email Address:", [validators.DataRequired(), validators.Email()])
    password = PasswordField("Password:", [validators.DataRequired()])
    password_verify = PasswordField("Verify Password:", [validators.DataRequired(), validators.equal_to("password")])
