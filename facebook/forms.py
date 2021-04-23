from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms import StringField, PasswordField, SubmitField, RadioField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed
from facebook.models import User


class RegistrationForm(FlaskForm):
    f_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "First Name"})
    l_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Last Name"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female')])
    dob = DateField('Date of Birth', format='%Y-%m-%d', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already in use, choose another email')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[
        DataRequired(), Length(min=1, max=140)], render_kw={"placeholder": "What's on your mind ?"})
    post_image = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit')


class EditPostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[
        DataRequired(), Length(min=1, max=140)], render_kw={"placeholder": "What's on your mind ?"})
    post_image = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit')


class EditProfilePhotoForm(FlaskForm):
    cover_image = FileField('Add Cover Photo', validators=[FileAllowed(['jpg', 'png'])])
    profile_image = FileField('Add Profile Photo', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit')


class EditStoryForm(FlaskForm):
    story_image = FileField('Add Story', validators=[DataRequired(), FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit')


class EditProfileForm(FlaskForm):
    f_name = StringField('First Name', validators=[DataRequired()])
    l_name = StringField('Last Name', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')


class EditProfileDetailsForm(FlaskForm):
    school = StringField('School', validators=[DataRequired()])
    hometown = StringField('Home Town', validators=[DataRequired()])
    location = StringField('Current Location', validators=[DataRequired()])
    relationship = RadioField('Gender', choices=[('single', 'Single'), ('married', 'Married'), ('dating', 'Dating')])
    submit = SubmitField('Submit')


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('comment', validators=[
        DataRequired(), Length(min=1, max=140)], render_kw={"placeholder": "Write a Comment"})
    submit = SubmitField('Submit')


class LikeForm(FlaskForm):
    like = TextAreaField('comment', validators=[
        DataRequired(), Length(min=1, max=140)], render_kw={"placeholder": "Write a Comment"})
    submit = SubmitField('Submit')


class MessageForm(FlaskForm):
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=0, max=140)], render_kw={"placeholder": "Type your message"})
    image = FileField('Add Photo', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit')


class RecipientList(FlaskForm):
    recipient = SelectField('Select the recipient', validators=[DataRequired()])
    submit = SubmitField('Submit')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')
