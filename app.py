from flask import Flask, jsonify
from controllers.inventory_controller import inventory_service
from models.db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://testing:testing@mysql/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# integrar instancia de base de datos 
db.init_app(app)
app.register_blueprint(inventory_service)
