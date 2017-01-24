from run import db


class RetailerContactPerson(db.Model):
    contact_person_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String, nullable=False)
    e_mail = db.Column(db.String)
    telephone = db.Column(db.String)
    fax = db.Column(db.String)