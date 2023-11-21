from flask_sqlalchemy.model import Model
from wtforms import IntegerField, StringField


class User(Model):
    id = IntegerField('id')
    name = StringField('name')
