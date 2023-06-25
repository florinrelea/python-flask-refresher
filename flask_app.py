from flask import Flask
from flask_marshmallow import Marshmallow
import os
from flask_jwt_extended import JWTManager
from flask_mail import Message

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'planets.db')
app.config['JWT_SECRET_KEY'] = 'thesecret'
app.config['MAIL_SERVER'] = 'test'
app.config['MAIL_USERNAME'] = 'test' # os.environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = 'test' # os.environ['MAIL_PASSWORD']

ma = Marshmallow(app)
jwt = JWTManager(app)

# mail = Mail(app)

# Test replacement for mail
class TestMail:
  def __init__(self):
    pass

  def send(self, msg: Message):
    print('Sending email')

mail = TestMail()