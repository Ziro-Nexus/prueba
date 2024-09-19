from flask import Blueprint, jsonify, request, render_template
from models.inventory_model import Inventory
from repository.inventory_repository import InventoryRepository
from models.db import db

inventory_service = Blueprint('inventory_service', __name__)

@inventory_service.route('/')
def index():
    """
    Render the index page with a list of all inventory items.

    Returns:
    HTML: Renders the 'index.html' template with all inventory items.
    """
    items = Inventory.query.all()
    return render_template('index.html', items=items)


@inventory_service.route('/<id>')
def get_by_id(id):
    """
    Retrieve an inventory item by its ID.

    Parameters:
    id (int): The ID of the inventory item to retrieve.

    Returns:
    JSON: The retrieved inventory item in JSON format.
    
    Raises:
    Exception: If the item with the given ID does not exist, a 201 status code with an error message is returned.
    """
    try:
        item = InventoryRepository.get_inventory_item_by_id(id=id)
        return item.as_json()
    except Exception as e:
        return jsonify({'message': str(e)}), 201


@inventory_service.route('/add', methods=["POST"])
def add():
    """
    Add a new inventory item to the database.
    
    Request Body:
    JSON: A dictionary containing details of the item to be added.

    Returns:
    JSON: The newly added inventory item in JSON format with a 201 status code.
    
    Raises:
    ValueError: If the provided data is invalid, returns a 400 status code.
    Exception: For other errors, returns a 500 status code.
    """
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
    """
    Delete an inventory item by its ID.

    Parameters:
    id (int): The ID of the inventory item to delete.

    Returns:
    JSON: A confirmation message in JSON format.
    
    Raises:
    Exception: If the item does not exist, returns a 201 status code with an error message.
    """
    try:
        item = InventoryRepository.delete_inventory_item_by_id(id=id)
        return item
    except Exception as e:
        return jsonify({'message': str(e)}), 201


@inventory_service.route('/edit/<id>', methods=["PUT"])
def edit(id):
    """
    Edit an existing inventory item with new data.

    Parameters:
    id (int): The ID of the inventory item to update.
    
    Request Body:
    JSON: A dictionary containing updated details of the item.

    Returns:
    JSON: The updated inventory item in JSON format.
    
    Raises:
    ValueError: If the provided data is invalid, returns a 400 status code.
    Exception: For other errors, returns a 500 status code.
    """
    try:
        data = request.get_json()
        item = InventoryRepository.edit_inventory_item(id=id, inventory_json=data)
        return item.as_json()
    except ValueError as ve:
        return jsonify({'message': str(ve)}), 400
    except Exception as e:
        return jsonify({'message': str(e)}), 500
