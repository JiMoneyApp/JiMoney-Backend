import os
from database import db
from dotenv import load_dotenv
from flask import Flask, jsonify



app = Flask(__name__)
load_dotenv()
db.init_app(app)


app.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")
app.config["MYSQL_PORT"] = int(os.getenv("MYSQL_PORT"))
app.config["MYSQL_USER"] = os.getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = os.getenv("MYSQL_DB")




if __name__ == "__main__":
    app.run(debug=True)