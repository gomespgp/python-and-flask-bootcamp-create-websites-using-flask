from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of Puppy:')
    submit = SubmitField('Add Puppy')

class DeleteForm(FlaskForm):

    id = IntegerField('Id Number Of Puppy to Remove:')
    submit = SubmitField('Remove Puppy')