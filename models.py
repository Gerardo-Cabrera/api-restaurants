from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    rating = db.Column(db.Integer)
    name = db.Column(db.String(50))
    site = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    street = db.Column(db.String(100))
    city = db.Column(db.String(50))
    state = db.Column(db.String(30))
    lat = db.Column(db.Numeric)
    lng = db.Column(db.Numeric)
