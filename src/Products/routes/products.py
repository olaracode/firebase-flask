from flask import Blueprint, request, jsonify
from Server.database import db
from Products.models.product import Product
from Helpers.handlers import error_handler

product = Blueprint('product', __name__)

@product.route('/create', methods=['POST'])
def create_product():
    body = request.json
    name = body.get('name', None)
    description = body.get('description', None)
    price = body.get('price', None)

    if not name or not description or not price:
        return error_handler('All fields are required', 400)

    new_product = Product(name=name, description=description, price=price, user_id=1)
    db.session.add(new_product)
    try:
        db.session.commit()
        return jsonify({'Product': new_product.serialize()})

    except Exception as error:
        db.session.rollback()
        return error_handler(error.args, 500)

@product.route('/', methods=['GET'], )
def get_products():
    products = Product.query.all()

    if not products:
        return error_handler('No products found', 404)

    return jsonify({"products": list(map(lambda product: product.serialize(), products))}), 200