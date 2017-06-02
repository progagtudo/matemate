from sqlalchemy import ForeignKey
from run import db


class Charge(db.Model):
    charge_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, ForeignKey("customer.customer_id"), nullable=False)
    staff_id = db.Column(db.Integer, ForeignKey("staff.staff_id"), nullable=False)
    charge_date = db.Column(db.DateTime, nullable=False)  # could make this unique
    donation = db.Column(db.Boolean, nullable=False)
    charge_amount = db.Column(db.Integer, nullable=False)  # should be decimal?
