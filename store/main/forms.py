from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, DecimalField
from wtforms.validators import InputRequired



class CreateItem(FlaskForm):
    name = StringField(validators = [InputRequired()])
    price = DecimalField(validators = [InputRequired()])
    stock = IntegerField(validators = [InputRequired()])
    submit = SubmitField('create')


class RestockItems(FlaskForm):
    addition = IntegerField(validators=[InputRequired()])
    submit = SubmitField('Confirm Restock')


class ModifyItem(FlaskForm):
    submit = SubmitField('apply')