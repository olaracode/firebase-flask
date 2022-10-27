import enum
from Products.models.product import Product
from Server.database import db
from Helpers.handlers import serialize_array

class Status(enum.Enum):
    active = "active"
    paid = "paid"
    sent = "sent"
    delivered = "delivered"
    canceled = "canceled"

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Enum(Status), default=Status.active)
    value = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    products = db.relationship('OrderProduct')

    def serialize(self):
        products = self.get_products()
        return {
            "id": f'{self.id}',
            'status': f'{self.status.value}',
            'order_products': products, 
            'user_id': f'{self.user_id}'

        }
    
    def generate_value(self):
        products = OrderProduct.query.filter_by(order_ir = self.id).all()
        if products is None:
            self.value = 0
            return self.value
        value = 0
        for product in products:
            value += product.price
        self.value = value
        try:
            db.session.commit()
            return self.value
        except Exception as error:
            db.session.rollback()
            return error.args

    def get_products(self):
        order_products = OrderProduct.query.filter_by(order_id=self.id).all()
        if order_products is None:
            return 'No products in this order'
        return serialize_array(order_products)

class OrderProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    def serialize(self):
        product = Product.query.get(self.product_id).one_or_none()
        order = Order.query.get(self.order_id).one_or_none()
        return {
            'id': f'{self.id}',
            'order_id': f'{order.serialize()}',
            'product': f'{product.serialize()}'
        }