from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class RegistrationForm(FlaskForm):
    f_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    l_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female')])
    dob = DateField('Date of Birth', format='%Y-%m-%d')
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    '''def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already in use, choose another email')'''