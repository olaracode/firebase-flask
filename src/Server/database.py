from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Separated from app to avoid circular reference
migrate = Migrate()
db = SQLAlchemy()