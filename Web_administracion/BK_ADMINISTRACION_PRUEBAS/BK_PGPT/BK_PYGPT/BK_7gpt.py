from flask import Blueprint
from .routes import admin_dashboard

admin_blueprint = Blueprint('admin', __name__)

# Ruta para el dashboard administrativo
admin_blueprint.add_url_rule('/admin', view_func=admin_dashboard, methods=['GET'])
