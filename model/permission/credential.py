import datetime
from run import db
from sqlalchemy import ForeignKey


class Credential(db.Model):
    credential_id = db.Column(db.Integer, primary_key=True)
    username_id = db.Column(db.Integer, ForeignKey("username.username_id"), nullable=False)
    credential_secret = db.Column(db.LargeBinary)
    credential_type_id = db.Column(db.Integer, ForeignKey("credential_type"), nullable=False)
    is_sales_person_login = db.Column(db.Boolean, nullable=False)
    credential_create_date = db.Column(db.DateTime, nullable=False)
    last_password_change = db.Column(db.DateTime)
