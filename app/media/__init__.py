from flask import Blueprint

media = Blueprint('media', __name__, template_folder='templates', static_folder='static', static_url_path='/media/static')

from app.media import routes