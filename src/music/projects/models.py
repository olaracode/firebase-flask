from Server.database import db

# A project is a collection of songs that are each a new version of the same song. Is must be related to songs and users, it can have collaborators and it must have a name.


class Project(db.Model):
    __tablename__ = "project"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    songs = db.relationship("Song", backref="project", lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    collaborators = db.relationship(
        "User", secondary="collaborators", backref="projects", lazy=True
    )
    version = db.Column(db.Integer, nullable=False, default=1)

    def __repr__(self):
        return f"Project('{self.name}', '{self.version}')"

    def __str__(self):
        return f"{self.name} {self.version}"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "version": self.version,
            "user_id": self.user_id,
            "songs": [song.serialize() for song in self.songs],
            "collaborators": [
                collaborator.serialize() for collaborator in self.collaborators
            ],
        }
