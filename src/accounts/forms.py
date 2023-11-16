from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from src.accounts.models import User
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, BooleanField, DateTimeField, SubmitField
from wtforms.validators import DataRequired, Length

#register form for new user
class RegisterForm(FlaskForm):
    email = EmailField(
        "Email", validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        "Repeat password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )

    def validate(self, extra_validators=None):
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        if self.password.data != self.confirm.data:
            self.password.errors.append("Passwords must match")
            return False
        return True

    def test():
        return "test"

#box form for booking a box for the user
class BookBoxForm(FlaskForm):
		location = StringField('Location', validators=[DataRequired()])
		size = IntegerField('Size', validators=[DataRequired()])
		duration = IntegerField('Duration', validators=[DataRequired()])
		submit = SubmitField('Book Box')

# standard login for user
class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])