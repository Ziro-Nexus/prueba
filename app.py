from flask import Flask, jsonify
from controllers.inventory_controller import inventory_service
from controllers.container_controller import container_service
from models.db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://testing:testing@mysql/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

db.init_app(app)
app.register_blueprint(inventory_service, name="inventory")
app.register_blueprint(container_service, name="container")
