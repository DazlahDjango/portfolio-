from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    name = StringField(
        'Your Name',
        validators=[DataRequired(), Length(min=2, max=80)]
    )
    email = StringField(
        'Your Email',
        validators=[DataRequired(), Email(), Length(max=120)]
    )
    message = TextAreaField(
        'Message',
        validators=[DataRequired(), Length(min=10, max=3000)]
    )
    submit = SubmitField('Send Message')