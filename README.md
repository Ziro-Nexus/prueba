# Inventory Manager

Demostration handling CRUD operations in a dockerized python web app.

## Requirements
- Python
- Docker
- Mysql

## Main Libraries
- flask
- flask_sqlalchemy

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

Go to https://localhost:5000 to interact with the interface.

