from flask import render_template, url_for, redirect, request
from application import app, db
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

        db.session.add(new_playlist)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        print(form.errors)
    return render_template('createplaylist.html', title='Create Playlist', form=form)

@app.route("/home/updateplaylist/<int:cur_id>", methods=["GET", "POST"])
def update_playlist(cur_id):
    playlist_id=Playlists.query.filter_by(id=cur_id).first()
    form = UpdatePlaylistForm()
    if form.validate_on_submit():
        playlist_id.playlist_name = form.playlist_name.data
        playlist_id.author = form.author.data
        playlist_id.playlist_song1 = form.playlist_song1.data
        playlist_id.playlist_song2 = form.playlist_song2.data
        playlist_id.playlist_song3 = form.playlist_song3.data
        db.session.commit()
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.playlist_name.data = playlist_id.playlist_name
        form.author.data = playlist_id.author
        form.playlist_song1.data = playlist_id.playlist_song1
        form.playlist_song2.data = playlist_id.playlist_song2
        form.playlist_song3.data = playlist_id_song3
    return render_template('updateplaylist.html', title='Update Playlist', form=form)

@app.route("/home/deleteplaylist/<int:cur_id>", methods=["GET", "POST"])
def delete_playlist(cur_id):
    playlist_id=Playlists.query.filter_by(id=cur_id).first()
    db.session.delete(playlist_id)
    db.session.commit()
    return redirect(url_for('home'))
