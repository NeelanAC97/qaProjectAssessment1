from application import db
from datetime import datetime

class Playlists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    playlist_name = db.Column(db.String(30), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    playlist_song = db.relationship('Songs',
            secondary='playlist_songs',
            cascade = 'delete',
            backref=db.backref('playlist'),
            lazy='dynamic')
    def __repr__(self):
        return ''.join(['Playlist ID: ', str(self.id), '\r\n',
                        'Playlist Name: ', self.playlist_name, '\r\n',
                        'Author: ', self.author
                        ])

class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String(30), nullable=False)
    artists = db.Column(db.String(50), nullable=False)
    length = db.Column(db.Float, nullable=False)
    genre = db.Column(db.String(30), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    playlist_song = db.relationship('Playlists',
            secondary='playlist_songs',
            cascade = 'delete',
            backref=db.backref('song'),
            lazy='dynamic')    
    def __repr__(self):
        return ''.join([
            'Song ID: ', str(self.id), '\r\n',
            'Song Name: ', self.song_name, '\r\n',
            'Arist(s): ', self.artists, '\r\n',
            'Length: ', str(self.length), '\r\n',
            'Genre: ', self.genre
            ])

playlist_songs = db.Table('playlist_songs', db.Model.metadata,
    db.Column('playlist_id', db.Integer, db.ForeignKey('playlists.id')),
    db.Column('song_id', db.Integer, db.ForeignKey('songs.id'))
)

