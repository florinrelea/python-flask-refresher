from flask import Flask
from flask_marshmallow import Marshmallow
import os
from flask_jwt_extended import JWTManager

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'planets.db')
app.config['JWT_SECRET_KEY'] = 'thesecret'

ma = Marshmallow(app)
jwt = JWTManager(app)