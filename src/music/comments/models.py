from Server.database import db
from datetime import datetime

# A comment most belong to a song and a user, it must have content and creation date


class Comment(db.Model):
    __tablename__ = "comment"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    song_id = db.Column(db.Integer, db.ForeignKey("song.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Comment('{self.content}', '{self.creation_date}')"

    def __str__(self):
        return f"{self.content} {self.creation_date}"

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "creation_date": self.creation_date,
            "song_id": self.song_id,
            "user_id": self.user_id,
        }
