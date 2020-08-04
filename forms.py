from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL, AnyOf


animal_list = ["cat", "CAT", "Cat", "dog", "DOG", "Dog", "porcupine", "PORCUPINE", "Porcupine"]

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Name of Pet")
    species = StringField("Species of Pet", validators=[AnyOf(animal_list, message=None, values_formatter=None)])
    photo = StringField("Photo URL of Pet", validators=[URL(require_tld=True, message=None), Optional()])
    age = IntegerField("Age of Pet", validators=[NumberRange(min=0, max=30, message="The age must be between 0 and 30 years old.")])
    notes = StringField("Notes about Pet")
    available = BooleanField("Is Pet Avail?")
    


