from application import db
from datetime import datetime

class Artists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(30), nullable=False)
    bio = db.Column(db.String(500), nullable=False)
    artist_track = db.relationship('ArtistTracks', backref='author', lazy=True)
    def __repr__(self):
        return ''.join(['Artist ID: ', str(self.id), '\r\n',
                        'Artist Name: ', self.artist_name, '\r\n',
                        'Bio: ', self.bio
                        ])

class Tracks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    track_name = db.Column(db.String(30), nullable=False)
    length = db.Column(db.Float, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    artist_track = db.relationship('Artist Tracks', backref='author', lazy=True)
    def __repr__(self):
        return ''.join([
            'Track ID: ', str(self.id), '\r\n',
            'Track Name: ', self.track_name, '\r\n',
            'Length: ', self.length
            ])

Class ArtistTracks(db.Model):
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
    track_id = db.Column(db.Integer, db.ForeignKey('tracks.id'), nullable=False)
    artist_name = db.Column(db.String(30), db.ForeignKey('artists.artist_name'), nullable=False)
    track_name = db.Column(db.Integer, db.ForeignKey('tracks.track_name'), nullable=False)
    def __repr__(self):
        return ''.join([
            'Artist Name: ', self.artist_name, '\r\n',
            'Track Name:', self.track_name
            ])

