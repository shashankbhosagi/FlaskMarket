from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo,Email, DataRequired, ValidationError
from market.models import User 

class Registerform(FlaskForm):
    def validate_username(self, username_to_check): # this is a custom validator validate_<field_name>
        user = User.query.filter_by(username=username_to_check.data).first()  # this is a query to check if the username exists in the database
        if user:    # if the username exists in the database
            raise ValidationError('Username already exists! Please try a different username.')  # raise an error
    
    def validate_email_address(self, email_address_to_check): # this is a custom validator validate_<field_name>
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()  # this is a query to check if the email exists in the database
        if email_address:    # if the email exists in the database
            raise ValidationError('Email Address already exists! Please try a different email address.')
    

    username = StringField(label='User Name:' ,validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email:' ,validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:',validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create account')


class LoginForm(FlaskForm):
    username=StringField(label="User Name:", validators=[DataRequired()])
    password=PasswordField(label="Password:", validators=[DataRequired()]) 
    submit = SubmitField(label='Sign in')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')