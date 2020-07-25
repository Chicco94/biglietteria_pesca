from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class PreEstrazioneForm(FlaskForm):
    submit = SubmitField('Prendi un biglietto')

class PostEstrazioneForm(FlaskForm):
    submit = SubmitField('Estrai di nuovo')