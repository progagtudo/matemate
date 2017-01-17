from run import db
class AvailableRight(db.Model):
    right_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False),
    description = db.Column(db.String)

