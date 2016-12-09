from flask_wtf import Form
from wtforms import TextField, PassowordField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(Forms):
	username = TextField('Username', validators=[DataRequired()])
	password = passwordField('Password', validators=[DataRequired()])


class RegistrationForm(Form):
	username = TextField(
		'username',
		validators=[DataRequired(), Length(min=3, max=25)]
		)
	    email = TextField(
	    	'email',
	    	validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
	    )
	    password = PasswordField(
	    	'password',
	    	validators=[DataRequired(), Length(min=6, max=25)]
        )
        confirm = PasswordField(
           'Repeat password',
           validators=[
               DataRequired(), EquaTo('password', message='Passwords must match.')
           ]
        )

