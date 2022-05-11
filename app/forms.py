from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class reg_call(FlaskForm):
    bed_id = StringField('bed_id', validators=[DataRequired()])
    status = StringField('status')
    submit = SubmitField('Call')
