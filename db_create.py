from jex import db
from models import User

#create the database and the db tables
db.create_all()

#insert

#commit the changes
db.session.commit()