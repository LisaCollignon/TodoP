from sqlalchemy.orm import backref
from app import db
from app.auth import constants as USER
from flask_login import UserMixin

class User(db.Model, UserMixin):

  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), unique=True)
  email = db.Column(db.String(120), unique=True)
  password = db.Column(db.String(120))
  role = db.Column(db.SmallInteger, default=USER.USER)
  status = db.Column(db.SmallInteger, default=USER.NEW)
  todos = db.relationship('Todo', backref='user', lazy=True)

  def __init__(self, name=None, email=None, password=None):
    self.name = name
    self.email = email
    self.password = password

  def getStatus(self):
    return USER.STATUS[self.status]

  def getRole(self):
    return USER.ROLE[self.role]

  def __repr__(self):
    return f'<User {self.name}>'
