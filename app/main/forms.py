from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms import StringField,TextAreaField,SubmitField,SelectField,RadioField

class PitchForm(FlaskForm):
    content = TextAreaField('New Pitch')
    # category_id = SelectField('select category')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment_section_id = TextAreaField('New Comment')
    submit = SubmitField('Submit')
