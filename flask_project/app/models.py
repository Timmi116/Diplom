from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import base64

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(20))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(128))
    date_of_birth = db.Column(db.Date)
    place_of_birth = db.Column(db.String(100))
    address = db.Column(db.Text)
    biography = db.Column(db.Text)
    profile_picture = db.Column(db.LargeBinary)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)