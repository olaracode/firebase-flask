import enum
from Server.database import db
from Products.models.order import Order, Status
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
    products = db.relationship('Product', lazy=True)
    order = db.relationship('Order')

    def serialize(self):
        order = self.get_active_order()
        orders = self.get_orders()
        return {
            'id': f'{self.id}',
            'name': f'{self.name}',
            'email': f'{self.email}',
            'role': f'{self.role.value}',
            'orders': orders,
            'active_order': order
        }

    def cancel_order(self):
        active_order = self.get_active_order()
        active_order.status = Status.canceled
        try:
            db.session.commit()
            return active_order.status
        except Exception as error:
            db.session.rollback
            return error_handler(error.args, 500)
        

    def get_orders(self):
        user_orders = Order.query.filter_by(user_id=self.id).all()
        if user_orders is None:
            return 'No orders'
        return serialize_array(user_orders)

    def get_active_order(self):
        user_orders = Order.query.filter_by(user_id = self.id).all()
        if user_orders:
            for order in user_orders:
                if order.status == Status.active:
                    active_order = order
                    return active_order.serialize()
                                 
        return 'No active order'
