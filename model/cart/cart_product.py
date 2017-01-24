from run import db

# FIXME whats this class' use and why is it in the database?


class CartProduct(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
