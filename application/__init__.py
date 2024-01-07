from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)

from application import routes
