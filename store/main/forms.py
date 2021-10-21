from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, DecimalField, SelectField
from wtforms.validators import InputRequired
from ..models import Item



class CreateItem(FlaskForm):
    name = StringField(validators = [InputRequired()])
    price = DecimalField()
    stock = IntegerField()
    submit = SubmitField('create')


class RestockItems(FlaskForm):
    addition = IntegerField()
    submit = SubmitField('Confirm Restock')


# class AddToCart(FlaskForm):
#     id = IntegerField()
#     purchase_quantity = IntegerField()
#     submit = SubmitField('Add')