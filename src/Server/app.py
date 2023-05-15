from flask import Flask
from flask_admin import Admin
from flask_jwt_extended import JWTManager
from .database import db, migrate
from Users.routes import user
from music.songs.routes import song
from admin import create_admin


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("settings.py")
    db.init_app(app)
    migrate.init_app(app, db)
    jwt = JWTManager(app)
    create_admin(app)
    app.register_blueprint(user, url_prefix="/users")
    app.register_blueprint(song, url_prefix="/songs")

    @app.route("/")
    def hello():
        """
        Simple endpoint for testing the server
        ---
        responses:
            200:
                description: A simple hello world
                type: string
        """
        return "<h1>Hello</h1>"

    return app
