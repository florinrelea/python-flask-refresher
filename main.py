from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get('/')
def hello_world():
  return 'Hello, World!'


@app.get('/super_simple')
def super_simple():
  return jsonify(
    message = 'Hello from the Planetary API.'
  )


@app.get('/fake-news')
def fake_news():
  return jsonify(
    message = 'We don\'t have that.'
  ), 404


@app.get('/test-params')
def params():
  name = request.args.get('name')
  age = int(request.args.get('age'))

  if age < 18:
    return jsonify(
      message = 'Stop right there.'
    ), 401

  return jsonify(
    message = f'Welcome {name}! We now know you are {age}'
  ), 200

@app.get('/test-url-params/<string:name>/<int:age>')
def test_url_params(name: str, age: int):
  if age < 18:
    return jsonify(
      message = 'Stop right there.'
    ), 401

  return jsonify(
    message = f'Welcome {name}! We now know you are {age}'
  ), 200


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )

