from flask import render_template, request, redirect, url_for, flash, send_file
from app.invoices import invoices
from flask_login import login_required
from app import db
from app.invoices.models import Invoice
from app.invoices.forms import InvoiceForm
import io
from weasyprint import HTML


# Invoices list

@invoices.route('/')
@login_required
def index():
    invoices_list = Invoice.query.all()
    return render_template('invoice_list.html', invoices=invoices_list)