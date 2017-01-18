from run import db
class Storage(db.Model):
    storage_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String)
    is_sale_allowed = db.Column(db.Boolean, nullable=False)
