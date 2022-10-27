from flask import Flask
from flask_jwt_extended import JWTManager
from .database import db, migrate
from Users.routes import user
from Products.routes.products import product
from Products.routes.orders import order
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(product, url_prefix='/product')
    app.register_blueprint(order, url_prefix='/order')

    jwt = JWTManager(app)
    @app.route('/')
    def hello():
        return '<h1>Hello</h1>'
    return app
