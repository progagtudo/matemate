import datetime

from model.person.person import Person
from run import db


class Staff(db.Model):
    staff_id = db.Column(db.Integer, primary_key=True)
    base_balance = db.Column(db.Numeric, default=0, nullable=False)
    base_balance_date = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)
    added_date = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)
    active_staff = db.Column(db.DateTime, default=True, nullable=False)