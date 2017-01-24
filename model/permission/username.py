from sqlalchemy import ForeignKey

from run import db


class Person(db.Model):
    username_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    person_id = db.Column(db.Integer, ForeignKey("person.person_id"), nullable=False)
