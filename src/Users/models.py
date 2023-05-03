import enum
from Server.database import db
from Helpers.handlers import error_handler, serialize_array


class roles(enum.Enum):
    admin = "admin"
    user = "user"
    provider = "provider"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(180))
    email = db.Column(db.String(180), unique=True, nullable=False)
    role = db.Column(db.Enum(roles), nullable=False, default=roles.user)
    salt = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    songs = db.relationship("Song", backref="user", lazy=True)

    def serialize(self):
        return {
            "id": f"{self.id}",
            "name": f"{self.name}",
            "email": f"{self.email}",
            "role": f"{self.role.value}",
        }
