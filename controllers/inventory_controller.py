from flask import Blueprint, jsonify, request, render_template
from models.inventory_model import Inventory
from repository.inventory_repository import InventoryRepository
from models.db import db


inventory_service = Blueprint('inventory_service', __name__)

# debug route
@inventory_service.route('/')
def index():
    devices = Inventory.query.all()
    
    # Pass the devices list to the template
    return render_template('index.html', items=devices)


@inventory_service.route('/<id>')
def get_by_id(id):
    try:
        item = InventoryRepository.get_inventory_item_by_id(id = id)
        return item.as_json()
    except Exception as e:
        return jsonify({'message': str(e)}), 201
        

@inventory_service.route('/add', methods=["POST"])
def add():
    try:
        data = request.get_json()
        new_item = InventoryRepository.add_inventory_item(inventory_json=data)
        return new_item.as_json(), 201
    except ValueError as ve:
        return jsonify({'message': str(ve)}), 400
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@inventory_service.route('/delete/<id>', methods=["DELETE"])
def delete(id):
    try:
        item = InventoryRepository.delete_inventory_item_by_id(id = id)
        return item
    except Exception as e:
        return jsonify({'message': str(e)}), 201


@inventory_service.route('/edit/<id>', methods=["PUT"])
def edit(id):
    try:
        data = request.get_json()
        item = InventoryRepository.edit_inventory_item(id = id, inventory_json = data)
        return item.as_json()
    
    except ValueError as ve:
        return jsonify({'message': str(ve)}), 400
    except Exception as e:
        return jsonify({'message': str(e)}), 500
