from flask import Flask
from routes.todo_routes import action

def create_app():
    app = Flask(__name__)
    app.register_blueprint(action)
    return app