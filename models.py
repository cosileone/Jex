from jex import db


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<{0} "{1}">'.format(self.id, self.email)
