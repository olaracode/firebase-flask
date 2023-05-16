from flask import Blueprint, request, jsonify
from firebase import firebase_bucket
from Helpers.handlers import error_handler
from .models import Song
from Server.database import db
from flask_jwt_extended import jwt_required, get_jwt_identity

song = Blueprint("songs", __name__)


@song.route("/music", methods=["GET"])
def get_music():
    songs = Song.query.all()
    return jsonify([song.serialize() for song in songs]), 200


@song.route("/music", methods=["POST"])
@jwt_required()
def post_music():
    identity = get_jwt_identity()
    print(identity)
    form = request.form
    files = request.files
    if not form:
        return error_handler("No form data", 400)
    title = form.get("title")
    artist = form.get("artist")
    song = files.get("song")
    if not title or not artist or not song:
        return error_handler("Missing data", 400)

    # Upload song to firebase storage
    upload_url = firebase_bucket.upload_file(song, song.filename or title)
    if not upload_url:
        return error_handler("Error uploading song", 500)

    # Create Song Psql object
    song = Song(title=title, artist=artist, url=upload_url, user_id=identity.get("id"))

    # Save song to firestore
    try:
        db.session.add(song)
        db.session.commit()
        return jsonify({"message": "Music added"}), 201
    except Exception as e:
        return jsonify(error_handler(e, 500))


@song.route("/music/<id>", methods=["DELETE"])
@jwt_required()
def delete_music(id):
    # Get the music document from Firestore
    song = Song.query.get(id)
    if not song:
        return error_handler("Music not found", 404)

    if song.user_id != get_jwt_identity().get("id"):
        return error_handler("Unauthorized", 401)

    # Delete the music document
    file_path = song.url.split(firebase_bucket.name + "/")[1]
    db.session.delete(song)
    db.session.commit()

    # Delete the music file from Firebase Storage
    firebase_bucket.delete_file(file_path)

    return jsonify({"message": "Music deleted"}), 200
