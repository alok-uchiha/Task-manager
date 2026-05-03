from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegisterForm(FlaskForm):
    username = StringField(
        "username",
        validators=[DataRequired(message="Username requried"), Length(min=3, max=50)]
    )
    email = StringField(
        "email",
        validators=[DataRequired(message="email requried"), Email(message="email requried")]
    )
    password = PasswordField(
        "password",
        validators=[DataRequired(message="password requried"), Length(min=6, message="minimum 6 chars.")]
    )
    confirm_password= PasswordField(
        "password",
        validators=[DataRequired(message="password requried"), EqualTo("password", message="password dint match")]
    )
    submit= SubmitField(
        "submit",
    )


class LoginForm(FlaskForm):
    email = StringField(
        "email",
        validators=[DataRequired(message="email requried"), Email()]
    )
    password= PasswordField(
        "password",
        validators=[DataRequired(message="password requried")]
    )
    submit= SubmitField(
        "submit"
    )
