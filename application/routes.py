from flask import render_template, url_for, redirect, request
from application import app, db, bcrypt
from application.models import Artists, Tracks, ArtistTracks
from application.forms import UploadTrackForm

@app.route('/home')
@app.route('/')
def home():
    all_tracks = Tracks.query.all()
    return render_template('home.html', title='Home', tracks=all_tracks)

@app.route('/uploadtrack', methods=['GET', 'POST'])
def upload_track():
    form = UploadTrackForm()
    if form.validate_on_submit():
        new_track = Tracks(
            track_name = form.track_name.data,
            length = form.length.data,
            genre = form.genre.data,
            
        )
        db.session.add(new_track)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        print(form.errors)
    return render_template('uploadtrack.html', title='Upload Track', form=form)
