from application import db
from application.models import Tracks, Artists, ArtistTracks

db.drop_all()
db.create_all()