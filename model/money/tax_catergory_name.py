from run import db


class TaxCategoryName(db.Model):
    tax_category_id = db.Column(db.Integer, primary_key=True)
    base_value = db.Column(db.Integer, nullable=False)
    base_value_unit = db.Column(db.Integer, nullable=False)
