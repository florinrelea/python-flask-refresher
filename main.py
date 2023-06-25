from flask import jsonify, request
from models import Planet
from flask_app import app
import cli_commands
from models import User
from db import db
from flask_jwt_extended import create_access_token

cli_commands.init(app)

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


@app.get('/planets')
def get_planets():
  planets_list = Planet.query.all()

  return jsonify(
    data = planets_list
  )

if __name__ == '__main__':
  app.run(
    debug=True,
    port=5000
  )

