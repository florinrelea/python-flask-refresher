from flask import jsonify, request
from models import Planet, planet_schema, planets_schema
from flask_app import app, mail
import cli_commands
from models import User
from db import db
from flask_jwt_extended import create_access_token
from flask_mail import Mail, Message

cli_commands.init(app)

@app.post('/retrieve-password/<string:email>')
def retrieve_password(email: str):
  user = User.query.filter_by(email=email).first()

  if user == None:
    # Fake response
    return jsonify(
      message='Password successfully sent!'
    ), 200


  msg = Message(
    "your planetary api password is " + user.password,
    sender='admin@planetary-api.com',
    recipients=[user.email]
  )

  mail.send(msg)

  return jsonify(
    message='Password successfully sent!'
  ), 200



@app.post('/login')
def login():
  email = request.json['email']
  password = request.json['password']

  found_user = User.query.filter_by(email=email, password=password).first()

  if found_user == None:
    return jsonify(
      message='Incorrect email or password.'
    ), 401

  new_access_token = create_access_token(identity=found_user.id)

  return jsonify(
    message = "Login succeeded!",
    access_token = new_access_token
  )


@app.post('/register')
def register():
  email = request.form['email']

  user_exists = User.query.filter_by(email=email).first()

  if user_exists:
    return jsonify(
      message='This email has already been taken.'
    ), 409

  first_name = request.form['first_name']
  last_name = request.form['last_name']
  password = request.form['password']

  new_user = User(
    email=email,
    first_name=first_name,
    last_name=last_name,
    password=password
  )

  db.session.add(new_user)
  db.session.commit()

  return jsonify(
    message = 'User created successfully.',
  ), 201


@app.post('/create-planet')
def create_planet():
  name = request.json['name']
  planet_type = request.json['planet_type']
  home_star = request.json['home_star']
  mass = float(request.json['mass'])
  radius = float(request.json['radius'])
  distance = float(request.json['distance'])

  found_existing_planet = Planet.query.filter_by(name=name).first()

  if found_existing_planet:
    return jsonify(
      message='This planet already exists.'
    ), 409

  new_planet = Planet(
    name=name,
    planet_type=planet_type,
    home_star=home_star,
    mass=mass,
    radius=radius,
    distance=distance
  )

  db.session.add(new_planet)
  db.session.commit()

  return jsonify(
    message = 'Planet created successfully.',
  ), 201

@app.delete('/planets/<int:planet_id>')
def delete_planet(planet_id: int):
  planet = Planet.query.filter_by(id=planet_id).first()

  if planet == None:
    return jsonify(
      message = 'Planet not found.'
    ), 404

  db.session.delete(planet)
  db.session.commit()

  return jsonify(
    message = 'Planet deleted successfully.',
  ), 202


@app.patch('/planets/<int:planet_id>')
def update_planet(planet_id: int):
  planet = Planet.query.filter_by(id=planet_id).first()

  if planet == None:
    return jsonify(
      message = 'Planet not found.'
    ), 404

  planet.name = request.json['name']
  planet.planet_type = request.json['planet_type']
  planet.home_star = request.json['home_star']
  planet.mass = float(request.json['mass'])
  planet.radius = float(request.json['radius'])
  planet.distance = float(request.json['distance'])

  db.session.commit()

  return jsonify(
    message = 'Planet updated successfully.',
  ), 202

@app.get('/planets/<int:planet_id>')
def get_planet(planet_id: int):
  planet = Planet.query.filter_by(id=planet_id).first()

  if planet:
    return jsonify(
      data = planet_schema.dump(planet)
    ), 200
  else:
    return jsonify(
      message = 'Planet not found.'
    ), 404


@app.get('/planets')
def get_planets():
  planets_list = Planet.query.all()

  return jsonify(
    data = planets_schema.dump(planets_list)
  )


if __name__ == '__main__':
  app.run(
    debug=True,
    port=5000
  )

