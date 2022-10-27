import enum
from Server.database import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String, nullable=True)
    price = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    
    def serialize(self):
        return {
            'id': f'{self.id}',
            'name': f'{self.name}',
            'description': f'{self.description}',
            'price': f'{self.price}',
            'user_id': f'{self.user_id}'
        }

