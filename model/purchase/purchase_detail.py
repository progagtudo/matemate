from sqlalchemy import ForeignKey
from run import db


class PurchaseDetail(db.Model):
    purchase_detail_id = db.Column(db.Integer, primary_key=True)
    purchase_id = db.Column(db.Integer, ForeignKey("purchase_header.purchase_id"), nullable=False)
    product_id = db.Column(db.Integer, ForeignKey("product.product_id"), nullable=False)
    order_amount = db.Column(db.Integer, nullable=False)
    is_shipped = db.Column(db.Boolean, nullable=False)
    purchase_amount = db.Column(db.Integer)
    best_before_date = db.Column(db.Date)
    prime_cost_per_unit = db.Column(db.Integer, nullable=False)
    tax_category_id = db.Column(db.Integer, ForeignKey("tax_category_name.tax_category_id"), nullable=False)
