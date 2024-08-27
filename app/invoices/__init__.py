from flask import Blueprint

invoices = Blueprint('invoices', __name__, template_folder='templates', static_folder='static')

from app.invoices import routes
