from flask import jsonify
from models.inventory_model import Inventory
from models.db import db

class InventoryRepository:
    
    
    def edit_inventory_item(id, inventory_json = {}):
        
        existing = Inventory.query.filter_by(id = id).first()
        if existing is None:
            raise Exception("Element does not exist")
        else:
            existing.name = inventory_json["name"]
            existing.price = inventory_json["price"]
            existing.mac_address = inventory_json["mac_address"]
            existing.serial_number = inventory_json["serial_number"]
            existing.manufacturer= inventory_json["manufacturer"]
            existing.description = inventory_json["description"]
            
            db.session.commit()
            
            return existing
    
    
    def add_inventory_item(inventory_json = {}):
        
        existing = Inventory.query.filter_by(name = inventory_json["name"]).first()
        
        if existing is None:
            new_item = Inventory(
                name = inventory_json["name"],
                price = inventory_json["price"],
                mac_address = inventory_json["mac_address"],
                serial_number = inventory_json["serial_number"],
                manufacturer= inventory_json["manufacturer"],
                description = inventory_json["description"]
            )
            db.session.add(new_item)
            db.session.commit()
            
            return new_item
        else:
            raise Exception("Already existing item name")

    def get_inventory_item_by_id(id):
        existing = Inventory.query.filter_by(id = id).first()
        if existing is None:
            raise Exception("Element does not exist")
        else:
            return existing
        
    def delete_inventory_item_by_id(id):
        existing = Inventory.query.filter_by(id = id).first()
        if existing is None:
            raise Exception("Element does not exist")
        else:
            db.session.delete(existing)
            db.session.commit()
            return jsonify({'message': "Item deleted succesfully"})
        