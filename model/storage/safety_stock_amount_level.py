from run import db


class SafetyStockAmountLevel(db.Model):
    safety_stock_amount_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
