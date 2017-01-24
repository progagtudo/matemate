import datetime

from sqlalchemy import ForeignKey

from run import db
from model.person.person import Person


class Customer(db.Model):
    customer_id = db.Column(db.Integer, ForeignKey("person.person_id"), primary_key=True)
    base_balance = db.Column(db.Numeric, default=0, nullable=False)
    base_balance_date = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)
    added_date = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)
    active_staff = db.Column(db.DateTime, default=True, nullable=False)