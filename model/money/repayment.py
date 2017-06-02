from sqlalchemy import ForeignKey
from run import db


class Repayment(db.Model):
    repayment_id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer, ForeignKey("staff.staff_id"), nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False)  # could make this unique
    amount = db.Column(db.Integer, nullable=False)  # should be decimal?
    required_amount_redeemers = db.Column(db.Integer, nullable=False)
