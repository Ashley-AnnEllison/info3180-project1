from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms import TextAreaField
from wtforms import RadioField
from wtforms import SelectField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired
from wtforms.validators import Email


class propertyForm(FlaskForm):
    title = TextField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    bedroom = TextField('No. of Rooms', validators=[DataRequired()])
    bathroom = TextField('No. of Bathroom', validators=[DataRequired()])
    price = TextField('Price', validators=[DataRequired()])
    type = SelectField('Property Type', choices=[('apartment', 'Apartment'), ('house', 'House')], validators=[DataRequired()])
    location = TextField('Location', validators=[DataRequired()])
    filename = TextField('Filename', validators=[DataRequired()])
    image =  FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])