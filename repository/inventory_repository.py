from flask import jsonify
from models.inventory_model import Inventory
from models.db import db

class InventoryRepository:
    
    def edit_inventory_item(id, inventory_json = {}):
        """
        Update an existing inventory item by ID with new data provided in inventory_json.
        
        Parameters:
        id (int): The ID of the inventory item to be updated.
        inventory_json (dict): A dictionary containing updated values for the item.
        
        Returns:
        Inventory: The updated inventory item object.
        
        Raises:
        Exception: If no item with the given ID is found.
        """
        existing = Inventory.query.filter_by(id=id).first()
        if existing is None:
            raise Exception("Element does not exist")
        else:
            existing.name = inventory_json["name"]
            existing.price = inventory_json["price"]
            existing.mac_address = inventory_json["mac_address"]
            existing.serial_number = inventory_json["serial_number"]
            existing.manufacturer = inventory_json["manufacturer"]
            existing.description = inventory_json["description"]
            db.session.commit()
            return existing
    
    def add_inventory_item(inventory_json = {}):
        """
        Add a new inventory item to the database if an item with the same name does not already exist.
        
        Parameters:
        inventory_json (dict): A dictionary containing the details of the item to be added.
        
        Returns:
        Inventory: The newly added inventory item object.
        
        Raises:
        Exception: If an item with the same name already exists.
        """
        existing = Inventory.query.filter_by(name=inventory_json["name"]).first()
        if existing is None:
            new_item = Inventory(
                name=inventory_json["name"],
                price=inventory_json["price"],
                mac_address=inventory_json["mac_address"],
                serial_number=inventory_json["serial_number"],
                manufacturer=inventory_json["manufacturer"],
                description=inventory_json["description"]
            )
            db.session.add(new_item)
            db.session.commit()
            return new_item
        else:
            raise Exception("Already existing item name")

    def get_inventory_item_by_id(id):
        """
        Retrieve an inventory item by its ID.
        
        Parameters:
        id (int): The ID of the inventory item to retrieve.
        
        Returns:
        Inventory: The retrieved inventory item object if found.
        
        Raises:
        Exception: If no item with the given ID is found.
        """
        existing = Inventory.query.filter_by(id=id).first()
        if existing is None:
            raise Exception("Element does not exist")
        else:
            return existing

    def delete_inventory_item_by_id(id):
        """
        Delete an inventory item by its ID.
        
        Parameters:
        id (int): The ID of the inventory item to delete.
        
        Returns:
        jsonify: A JSON response confirming the deletion.
        
        Raises:
        Exception: If no item with the given ID is found.
        """
        existing = Inventory.query.filter_by(id=id).first()
        if existing is None:
            raise Exception("Element does not exist")
        else:
            db.session.delete(existing)
            db.session.commit()
            return jsonify({'message': "Item deleted successfully"})
