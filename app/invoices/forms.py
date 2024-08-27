from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DecimalField, DateField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class InvoiceForm(FlaskForm):
    invoice_to = StringField('Invoice To', validators=[DataRequired()])
    attention = StringField('ATTN', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    amount = DecimalField('Amount', places=2, validators=[DataRequired(), NumberRange(min=0)])
    sub_total = DecimalField('Sub Total', places=2, validators=[DataRequired(), NumberRange(min=0)])
    total_amount = DecimalField('Total Amount', places=2, validators=[DataRequired(), NumberRange(min=0)])
    due_date = DateField('Due Date', format='%Y-%m-%d', validators=[DataRequired()])
    is_paid = BooleanField('Paid')
    submit = SubmitField('Create Invoice')
