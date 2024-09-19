# Inventory Manager

Demostration handling CRUD operations in a dockerized python web app.

## Requirements
- Python
- Docker
- Free 3306 port for dv

## Main Libraries
- flask
- flask_sqlalchemy

## Routes
- "/" -> Jinja2 template that list all object with interactive buttons to edit and delete
- "/{id}" -> Get inventory item by id
- "/add" -> Accepts JSON, add new inventory item
- "/edit/{id}" -> Accepts JSON, update existing inventory item by id
- "/delete/{id}" -> Delete existing inventory item by id

## Explanation of folders
- Controllers: folder that contain controller files to handle the route of the API
- models: folder that contain all the models defined in the database and configured with SQlAlchemy
- Repository: folder that contain all the logic used in the controllers
- db_dump: contain initial script for the database of the application
- static: static files used in our template
- templates: jinja2 templates of the application

## how to run
```bash
docker-compose up --build
```

- wait until mysql is ready
```bash
mysql-1  | 2024-09-19T12:37:32.953841Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '9.0.1'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server - GPL. 
```

- Go to http://localhost:5000 to interact with the interface.

- DB credentials
    - username: testing
    - password: testing

