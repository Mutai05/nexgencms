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
    return render_template('invoices/invoice_list.html', invoices=invoices_list)

# Create invoice

@invoices.route('/create', methods=['GET', 'POST'])
@login_required
def new():
    form = InvoiceForm()
    if form.validate_on_submit():
        new_invoice = Invoice(
            invoice_to=form.invoice_to.data,
            attention=form.attention.data,
            description=form.description.data,
            amount=form.amount.data,
            sub_total=form.sub_total.data,
            total_amount=form.total_amount.data,
            due_date=form.due_date.data,
            is_paid=form.is_paid.data
        )
        db.session.add(new_invoice)
        db.session.commit()
        
        flash('Invoice created successfully!', 'success')
        return redirect(url_for('invoices.index'))
    
    return render_template('invoices/new_invoice.html', form=form)

# View invoice

@invoices.route('/invoice/<int:invoice_id>')
@login_required
def view_invoice(invoice_id):
    invoice = Invoice.query.get_or_404(invoice_id)
    return render_template('invoices/single_invoice.html', invoice=invoice)

# Generate Invoice PDF

@invoices.route('/invoice/<int:invoice_id>/pdf')
@login_required
def generate_pdf(invoice_id):
    invoice = Invoice.query.get_or_404(invoice_id)
    rendered = render_template('invoices/invoice_pdf.html', invoice=invoice)
    
    pdf = HTML(string=rendered).write_pdf()
    
    # Dynamically generate the filename based on the invoice_to field
    filename = f"{invoice.invoice_to.replace(' ', '_')}.pdf"
    
    response = send_file(
        io.BytesIO(pdf),
        as_attachment=True,
        download_name=filename,
        mimetype='application/pdf'
    )
    return response

# Delete invoice 

@invoices.route('/delete/<int:invoice_id>', methods=['POST'])
@login_required
def delete_invoice(invoice_id):
    invoice = Invoice.query.get_or_404(invoice_id)
    db.session.delete(invoice)
    db.session.commit()
    flash('Invoice has been deleted successfully.', 'success')
    return redirect(url_for('invoices.index'))
