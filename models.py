from sqlalchemy import Column, Integer, String, Float
from db import db
from flask_app import ma

class User(db.Model):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  first_name = Column(String)
  last_name = Column(String)
  email = Column(String, unique=True)
  password = Column(String)


class UserSchema(ma.Schema):
  class Meta:
    fields = ('id', 'first_name', 'last_name', 'email', 'password')

class Planet(db.Model):
  __tablename__ = 'planets'
  id = Column(Integer, primary_key=True)
  name = Column(String)
  planet_type = Column(String)
  home_star = Column(String)
  mass = Column(Float)
  radius = Column(Float)
  distance = Column(Float)



class PlanetSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'planet_type', 'home_star', 'mass', 'radius', 'distance')


user_schema = UserSchema()
users_schema = UserSchema(many=True)

planet_schema = PlanetSchema()
planets_schema = PlanetSchema(many=True)
