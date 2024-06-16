import os
from flask import Flask, jsonify
from data import data
from user import user
from ledger import ledger

app = Flask(__name__)

app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(ledger, url_prefix="/ledger")
app.register_blueprint(data, url_prefix="/data")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
