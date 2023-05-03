from flask import Blueprint, request, jsonify
from .firebase import bucket
from Helpers.handlers import error_handler
from .models import Song
from Server.database import db
from flask_jwt_extended import jwt_required, get_jwt_identity

firebase = Blueprint("firebase", __name__)


@firebase.route("/music", methods=["GET"])
def get_music():
    songs = Song.query.all()
    return jsonify([song.serialize() for song in songs]), 200


@firebase.route("/music", methods=["POST"])
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
    blob = bucket.blob(song.filename)  # Create blob(Basicamente)
    blob.upload_from_file(song)
    blob.make_public()
    # Create Song Psql object
    song = Song(
        title=title, artist=artist, url=blob.public_url, user_id=identity.get("id")
    )
    # Save song to firestore
    try:
        db.session.add(song)
        db.session.commit()
        return jsonify({"message": "Music added"}), 201
    except Exception as e:
        return jsonify(error_handler(e, 500))


@firebase.route("/music/<id>", methods=["DELETE"])
@jwt_required()
def delete_music(id):
    # Get the music document from Firestore
    song = Song.query.get(id)
    if not song:
        return error_handler("Music not found", 404)

    if song.user_id != get_jwt_identity().get("id"):
        return error_handler("Unauthorized", 401)

    # Delete the music document
    file_path = song.url.split(bucket.name + "/")[1]
    db.session.delete(song)
    db.session.commit()
    # Get the music document from Firestore

    # Get the URL of the music file
    # Extract the file path from the URL

    # Delete the music file from Firebase Storage
    blob = bucket.blob(file_path)
    blob.delete()

    return jsonify({"message": "Music deleted"}), 200
