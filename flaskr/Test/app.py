import os
from flask import Flask, jsonify
from user import user

app = Flask(__name__)

app.register_blueprint(user, url_prefix="/user")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
