from run import db
class ClientType(db.Model):
    client_type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
#keine description?