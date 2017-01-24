import datetime

from run import db


class Person(db.Model):
    person_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)
    creation_date_time = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)
