from sqlalchemy import ForeignKey
from run import db


class TaxCategoryValue(db.Model):
    tax_category_id = db.Column(db.Integer, ForeignKey("tax_category_name.tax_category_id"), primary_key=True, nullable=False)
    valid_since = db.Column(db.Date, primary_key=True, nullable=False)
    value = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.Integer, nullable=False)
