from run import db


class CartProduct(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)