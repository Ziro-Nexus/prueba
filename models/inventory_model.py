from flask import jsonify
from models.db import db

class Inventory(db.Model):
    __tablename__ = 'Inventory'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Numeric(10, 2))
    mac_address = db.Column(db.String(17))
    serial_number = db.Column(db.String(255))
    manufacturer = db.Column(db.String(255))
    description = db.Column(db.Text)
    
    def as_json(self):
        return jsonify({c.name: getattr(self, c.name) for c in self.__table__.columns})
