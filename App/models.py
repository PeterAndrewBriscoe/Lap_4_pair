import string
from datetime import datetime
from random import choices
from . import db
from sqlalchemy.sql import func

class Urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(1000))
    shortened_url = db.Column(db.String(5), unique=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())    








