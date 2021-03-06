from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,Form
from wtforms.validators import Regexp,EqualTo,ValidationError,Length,InputRequired,URL,Email
from wtforms import TextField, PasswordField

## login and registration


class LoginForm(FlaskForm):
    username = TextField('username', id='username_login')
    password = PasswordField('password', id='pwd_login')


class CreateAccountForm(FlaskForm):
    username = TextField('username', id='username_create')
    password = PasswordField('password', id='pwd_create')
    password2 = PasswordField('password2', id='pwd_create')

class AddNewsForm(Form):
    title = StringField(validators=[InputRequired(message='请输入标题')])

