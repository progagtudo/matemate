
from run import db


class ProductCategory(db.Model):
    product_category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    category_icon_uri = db.Column(db.String)