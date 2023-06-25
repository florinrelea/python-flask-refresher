from sqlalchemy import Column, Integer, String, Float
from db import db

class User(db.Model):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  first_name = Column(String)
  last_name = Column(String)
  email = Column(String, unique=True)
  password = Column(String)


class Planet(db.Model):
  __tablename__ = 'planets'
  id = Column(Integer, primary_key=True)
  name = Column(String)
  planet_type = Column(String)
  home_star = Column(String)
  mass = Column(Float)
  radius = Column(Float)
  distance = Column(Float)
