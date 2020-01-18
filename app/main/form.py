from wtforms import StringField,SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import required

class commentform(FlaskForm):
    '''
    the comment form class
    '''
    body = StringField('enter your comment',validators=[Required()])
    submit = SubmitField('submit')