from sqlalchemy import ForeignKey
from run import db


class PurchaseHeader(db.Model):
    purchase_id = db.Column(db.Integer, primary_key=True)
    invoice_number = db.Column(db.Integer)  # whats dis?
    invoice_copy = db.Column(db.Binary)  # and dis?
    invoice_is_pre_tax = db.Column(db.Boolean, nullable=False)
    retailer_id = db.Column(db.Integer, ForeignKey("retailer.retailer_id"), nullable=False)
    staff_id = db.Column(db.Integer, ForeignKey("staff.staff_id"), nullable=False)
