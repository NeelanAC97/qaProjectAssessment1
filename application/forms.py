from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, FloatField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, NumberRange
from application.models import Songs, Playlists

class CreatePlaylistForm(FlaskForm):

    playlist_name = StringField('Playlist Name',
        validators = [
            DataRequired(),
            Length(min=3, max=30)
        ]
    )
    author = StringField('Author',
        validators = [
            DataRequired(),
            Length(min=3, max=50)
        ]
    )
    playlist_song1 = StringField('Song 1 Name',
        validators = [
            DataRequired(),
            Length(min=3, max=100)
        ]
    )
    playlist_song2 = StringField('Song 2 Name',
        validators = [
            DataRequired(),
            Length(min=3, max=100)
        ]
    )
    playlist_song3 = StringField('Song 3 Name',
        validators = [
            DataRequired(),
            Length(min=3, max=100)
        ]
    )
    submit = SubmitField('Create Playlist')

    def validate_song1(self,playlist_song1):
        valid_song=Songs.query.filter_by(song_name=playlist_song1.data).first()
        
        if not valid_song:
            raise ValidationError('Please enter a song from the list of songs!')
    
    def validate_song2(self,playlist_song2):
        valid_song=Songs.query.filter_by(song_name=playlist_song2.data).first()

        if not valid_song:
            raise ValidationError('Please enter a song from the list of songs!')

    def validate_song3(self,playlist_song3):
        valid_song=Songs.query.filter_by(song_name=playlist_song3.data).first()

        if not valid_song:
            raise ValidationError('Please enter a song from the list of songs!')

class UpdatePlaylistForm(FlaskForm):

    playlist_name = StringField('Playlist Name',
        validators = [
            DataRequired(),
            Length(min=3, max=30)
        ]
    )
    author = StringField('Author',
        validators = [
            DataRequired(),
            Length(min=3, max=50)
        ]
    )
    playlist_song1 = StringField('Song 1 Name',
        validators = [
            DataRequired(),
            Length(min=3, max=100)
        ]
    )
    playlist_song2 = StringField('Song 2 Name',
        validators = [
            DataRequired(),
            Length(min=3, max=100)
        ]
    )
    playlist_song3 = StringField('Song 3 Name',
        validators = [
            DataRequired(),
            Length(min=3, max=100)
        ]
    )
    submit = SubmitField('Create Playlist')

    def validate_song1(self,playlist_song1):
        valid_song=Songs.query.filter_by(song_name=playlist_song1.data).first()
        
        if not valid_song:
            raise ValidationError('Please enter a song from the list of songs!')
    
    def validate_song2(self,playlist_song2):
        valid_song=Songs.query.filter_by(song_name=playlist_song2.data).first()

        if not valid_song:
            raise ValidationError('Please enter a song from the list of songs!')

    def validate_song3(self,playlist_song3):
        valid_song=Songs.query.filter_by(song_name=playlist_song3.data).first()

        if not valid_song:
            raise ValidationError('Please enter a song from the list of songs!')





