from flask import Blueprint

users = Blueprint('users', __name__, template_folder='templates', static_folder='static', static_url_path='/users/static')

from app.users import routes