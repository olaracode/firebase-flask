from Server.database import db
from music.projects.models import Project

# a song is a version of a project. It must be related to a project and a user who created it, it can have comments and it must have a name and a version, the version most be unique for a project.


class Song(db.Model):
    __tablename__ = "song"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    version = db.Column(db.Integer, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    comments = db.relationship("Comment", backref="song", lazy=True)

    __table_args__ = (
        db.UniqueConstraint("project_id", "version", name="unique_project_version"),
    )

    def __repr__(self):
        return f"Song('{self.name}', '{self.version}')"

    def __str__(self):
        return f"{self.name} {self.version}"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "version": self.version,
            "project_id": self.project_id,
            "user_id": self.user_id,
            "comments": [comment.serialize() for comment in self.comments],
        }
