from sqlalchemy import ForeignKey

from run import db


class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.Numeric, nullable=False)
    is_sale_prohibited = db.Column(db.Boolean, nullable=False)
    is_default_redemption = db.Column(db.Boolean, nullable=False)
    tax_category_id = db.Column(db.Integer, ForeignKey("tax_category_name.tax_category_id"), nullable=False)
    product_category_id = db.Column(db.Integer, ForeignKey("product_category.product_category_id"))
