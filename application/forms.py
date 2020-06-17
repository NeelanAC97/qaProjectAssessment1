from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Users
from flask_login import current_user

class UplaodTrackForm(FlaskForm):

    track_name = StringField('Track Name',
        validators = [
            DataRequired(),
            Length(min=3, max=100)
        ]
    )
    length = StringField('Length',
        validators = [
            DataRequired(),
        ]
    )
    genre = StringField('Genre',
        validators = [
            DataRequired(),
            Length(min=3, max=100)
        ]
    )
    submit = SubmitField('Post!')
