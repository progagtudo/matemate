from sqlalchemy import ForeignKey
from run import db


class RedeemerFor(db.Model):
    staff_id = db.Column(db.Integer, ForeignKey("staff.staff_id"), nullable=False)
    repayment_id = db.Column(db.Integer, ForeignKey("repayment.repayment_id"), nullable=False)
    acknowledged_date = db.Column(db.DateTime, nullable=False)
