from flask import Blueprint, jsonify, request, render_template, redirect, url_for, flash
from models.db import db
from repository.container_repository import ContainerRepository
from models.container_model import Container
from models.inventory_model import Inventory
from sqlalchemy import func, case

container_service = Blueprint('inventory_service', __name__)

@container_service.route('/container', methods=['GET'])
def index_container():
    """
    Render the index page with a list of all inventory items.

    Returns:
    HTML: Renders the 'index.html' template with all inventory items.
    """
    containers_with_counts = (
        db.session.query(
            Container,
            func.sum(case((Inventory.id != None, 1), else_=0)).label('inventory_count')  # Conditional sum
        )
        .outerjoin(Container.inventories)  # Outer join with inventories
        .group_by(Container.container_id)  # Group by container ID
        .order_by(Container.container_id.desc())  # Latest containers first
        .limit(10)  # Limit to 10 results
        .all()
    )

    containers = [
    {
        'container': container,
        'inventory_count': inventory_count
    }
        for container, inventory_count in containers_with_counts
    ]
    return render_template('container.html', containers=containers)


@container_service.route("/container/add", methods=["POST"])
def add_container():

    new_container = ContainerRepository.add_container({"name": request.form.get("name"), 
                                              "status": request.form.get("status"), 
                                              "from_warehouse": request.form.get("from_warehouse"), 
                                              "to_warehouse": request.form.get("to_warehouse")}).as_json()
    
    flash(f"New container created", "alert alert-success")
    return redirect(url_for("container.index_container"))
