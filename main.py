from flask import jsonify, request
from flask_app import app
import cli_commands

cli_commands.init(app)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )

