from sqlalchemy import ForeignKey
from run import db


class Client(db.Model):
    client_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    client_type_id = db.Column(db.Integer, ForeignKey("client_type.client_type_id"), nullable=False)
    client_secret = db.Column(db.LargeBinary, nullable=False)
