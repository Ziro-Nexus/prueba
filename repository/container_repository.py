from flask import jsonify
from models.container_model import Container
from models.db import db

class ContainerRepository:

    def add_container(container_json = {}):
        new_item = Container(
            name = container_json["name"],
            status = container_json["status"],
            from_warehouse = container_json["from_warehouse"],
            to_warehouse = container_json["to_warehouse"]
        )
        db.session.add(new_item)
        db.session.commit()
        return new_item

