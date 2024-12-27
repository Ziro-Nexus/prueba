from flask import jsonify
from models.db import db

class Container(db.Model):
    __tablename__ = 'Container'
    container_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    status = db.Column(db.String(45))
    from_warehouse = db.Column(db.String(45))
    to_warehouse = db.Column(db.String(45))
    inventories = db.relationship('Inventory', backref='container', lazy=True)

    def as_json(self):
        return jsonify({c.name: getattr(self, c.name) for c in self.__table__.columns})
