from operator import ge
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from Server.database import db
from Helpers.handlers import error_handler, serialize_array
from Products.models.order import Order, Status
from Users.models import User

order = Blueprint('order', __name__)

@order.route('/all', methods=['GET'])
def get_all_orders():
    orders = Order.query.all()
    return jsonify({"orders": serialize_array(orders)})

@order.route('/', methods=['GET'])
@jwt_required()
def get_orders():
    user = User.query.get(get_jwt_identity()["id"])
    return jsonify({"user": user.serialize()["orders"]})
    
@order.route('/cancel', methods=['PUT'])
@jwt_required()
def cancel_order():
    user = User.query.get(get_jwt_identity()["id"])
    cancel_order = user.cancel_order()
    if cancel_order:
        return jsonify({"msg": "Order deleted successfully"})
    return error_handler('Something went  wrong', 500)

@order.route('/create', methods=['POST'])
@jwt_required()
def create_order():
    user_id = get_jwt_identity()

    order_exists = Order.query.filter_by(user_id=user_id["id"]).all()
    if order_exists:
        for order in order_exists:
            if order.status == Status.active:
                return error_handler('User already owns an order', 400)
 
    new_order = Order(user_id=user_id["id"])
    db.session.add(new_order)

    try:
        db.session.commit()
        return jsonify({'Order': new_order.serialize()})

    except Exception as error:
        db.session.rollback()
        return error_handler(error.args, 500)
    

