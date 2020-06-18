from application import db
from datetime import datetime

class Artists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(30), nullable=False)
    bio = db.Column(db.String(500), nullable=False)
    artist_track = db.relationship('Tracks',secondary='artist_tracks', backref='artist', lazy=True)
    def __repr__(self):
        return ''.join(['Artist ID: ', str(self.id), '\r\n',
                        'Artist Name: ', self.artist_name, '\r\n',
                        'Bio: ', self.bio
                        ])

class Tracks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    track_name = db.Column(db.String(30), nullable=False)
    length = db.Column(db.Float, nullable=False)
    genre = db.Column(db.String(30), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    artist_track = db.relationship('Artists',secondary='artist_tracks', backref='track', lazy=True)
    def __repr__(self):
        return ''.join([
            'Track ID: ', str(self.id), '\r\n',
            'Track Name: ', self.track_name, '\r\n',
            'Length: ', self.length
            ])

class ArtistTracks(db.Model):
    __tablename__="artist_tracks"
    artist_track_id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
    track_id = db.Column(db.Integer, db.ForeignKey('tracks.id'), nullable=False)
    def __repr__(self):
        return ''.join([
            'Artist ID: ', str(self.artist_id), '\r\n',
            'Track ID:', str(self.track_id)
            ])

