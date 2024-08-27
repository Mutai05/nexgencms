from flask import Blueprint

database = Blueprint('database', __name__, template_folder='templates', static_folder='static')

from app.database import routes
