from flask import jsonify

def error_handler(error_message, error_code):
    return jsonify({"error": error_message}), error_code

def serialize_array(object_array):
    return list(map(lambda item: item.serialize(), object_array))
