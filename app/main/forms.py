from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField,SelectField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError
from ..models import User


class ReasonForm(FlaskForm):
 title = StringField('Reason title',validators=[Required()])
 reason = TextAreaField('Reason for using Pomodoro',validators=[Required()])
 submit = SubmitField('Submit')
  

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')