from flask import render_template, url_for, redirect, request
from application import app, db, bcrypt
from application.models import Songs, Playlists
from application.forms import CreatePlaylistForm, UpdatePlaylistForm

@app.route('/home')
@app.route('/')
def home():
    all_playlists = Playlists.query.all()
    return render_template('home.html', title='Home', playlists=all_playlists)

@app.route('/songs')
def songs():
    all_songs = Songs.query.all()
    return render_template('songs.html', title='Songs', songs=all_songs)

@app.route('/createplaylist', methods=['GET', 'POST'])
def create_playlist():
    form = CreatePlaylistForm()
    if form.validate_on_submit():
        new_playlist = Playlists(
            playlist_name = form.playlist_name.data,
            author = form.author.data            
        )
        
        if form.playlist_song1.data != '':
            playlist_song1 = Songs.query.filter_by(song_name = form.playlist_song1.data).first()
            if playlist_song1:
                new_playlist.song.append(playlist_song1)
        
        if form.playlist_song2.data != '':
            playlist_song2 = Songs.query.filter_by(song_name = form.playlist_song2.data).first()
            if playlist_song2:
                new_playlist.song.append(playlist_song2)

        if form.playlist_song3.data != '':
            playlist_song3 = Songs.query.filter_by(song_name = form.playlist_song3.data).first()
            if playlist_song3:
                new_playlist.song.append(playlist_song3)

        #new_playlist.song.append(songs)
        db.session.add(new_playlist)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        print(form.errors)
    return render_template('createplaylist.html', title='Create Playlist', form=form)

@app.route("/home/updateplaylist", methods=["GET", "POST"])
def update_playlist():
    form = UpdatePlaylistForm()
    if form.validate_on_submit():
        playlist_name = form.playlist_name.data
        author = form.author.data
        playlist_song1 = form.playlist_song1.data
        playlist_song2 = form.playlist_song2.data
        playlist_song3 = form.playlist_song3.data
        db.session.commit()
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
    return redirect(url_for('home'))
