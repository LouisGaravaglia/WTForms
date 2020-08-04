from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, Email


# WTForms gives us lots of useful validators; we want to use these for validating our fields more carefully:

#     the species should be either “cat”, “dog”, or “porcupine”
#     the photo URL must be a URL (but it should still be able to be optional!)
#     the age should be between 0 and 30, if provided


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Name of Pet")
    species = StringField("Species of Pet")
    photo = StringField("Photo of Pet")
    age = IntegerField("Age of Pet")
    notes = StringField("Notes about Pet")
    available = BooleanField("Is Pet Avail?")
    


# class UserForm(FlaskForm):
#     """Form for adding/editing friend."""

#     name = StringField("Name",
#                        validators=[InputRequired()])
#     email = StringField("Email Address",
#                         validators=[Optional(), Email()])
