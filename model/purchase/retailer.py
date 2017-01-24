from run import db


class Retailer(db.Model):
    retailer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address_country = db.Column(db.String)
    address_zip_code= db.Column(db.String)
    address_city = db.Column(db.String)
    address_street = db.Column(db.String)
    address_street_number = db.Column(db.String)
    customer_number = db.Column(db.String)
    description = db.Column(db.String)
