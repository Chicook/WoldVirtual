from flask import Blueprint
from .routes import create_wallet, send, receive

wallet_blueprint = Blueprint('wallet', __name__)

# Rutas para wallet
wallet_blueprint.add_url_rule('/create', view_func=create_wallet, methods=['POST'])
wallet_blueprint.add_url_rule('/send', view_func=send, methods=['POST'])
wallet_blueprint.add_url_rule('/receive', view_func=receive, methods=['GET'])
