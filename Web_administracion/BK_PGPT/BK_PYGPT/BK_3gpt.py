from flask import Blueprint
from .routes import register, login

users_blueprint = Blueprint('users', __name__)

# Rutas para usuarios
users_blueprint.add_url_rule('/register', view_func=register, methods=['POST'])
users_blueprint.add_url_rule('/login', view_func=login, methods=['POST'])
