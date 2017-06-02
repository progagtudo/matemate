from sqlalchemy import ForeignKey
from run import db


# TODO Primary key correct?
class RedeemerFor(db.Model):
    staff_id = db.Column(db.Integer, ForeignKey("staff.staff_id"), nullable=False, primary_key=True)
    repayment_id = db.Column(db.Integer, ForeignKey("repayment.repayment_id"), nullable=False, primary_key=True)
    acknowledged_date = db.Column(db.DateTime, nullable=False)
