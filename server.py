from os import getenv
from dotenv import load_dotenv
from sys import exit as exitCode
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request
app = Flask(__name__)

# loading environments


load_dotenv()
env = [getenv("MYSQL_URI"), getenv("LABLE")]
if None in env:
    exitCode("Please set all environment")


app.config['SQLALCHEMY_DATABASE_URI'] = env[0]
db = SQLAlchemy(app)
db.create_all()


class PhoneNumber(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100), nullable=False)  # unique=True
    phone = db.Column("phonenumber", db.String(100),
                      unique=True, nullable=False)

    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone


@app.route("/")
def base():
    return "ARVAN"


@app.route('/phonenumber', methods=['GET'])
def getPhoneNumber():
    s = request.get_json()
    return jsonify(s), 204


@app.route('/phonenumber/<numberId>', methods=['GET'])
def getPhoneNumber(numberId: str = ""):
    s = request.get_json()
    return jsonify(s), 204


@app.route('/phonenumber', methods=['POST'])
def setPhoneNumber():
    s = request.get_json()
    return jsonify(s), 204


@app.route('/phonenumber/<numberId>', methods=['PUT'])
def putPhoneNumber(numberId: str = ""):
    s = request.get_json()
    return jsonify(s), 204


@app.route('/phonenumber/<numberId>', methods=['DELETE'])
def delPhoneNumber(numberId: str = ""):
    s = request.get_json()
    return jsonify(s), 204
