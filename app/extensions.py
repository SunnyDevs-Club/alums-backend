from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger

swagger = Swagger()

db = SQLAlchemy()
migrate = Migrate()
