from application import db
from application.models import Playlists, Songs

db.drop_all()
db.create_all()
