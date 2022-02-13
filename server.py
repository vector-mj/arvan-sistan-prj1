# from model import PhoneNumber

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request

from os import getenv
from dotenv import load_dotenv
from sys import exit as exitCode


# loading environments
load_dotenv()
env = [getenv("MYSQL_URI"), getenv("LABLE")]
if None in env:
    exitCode("Please set all environment")

# flask app with db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = env[0]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
try:
    db.engine.execute("select 1")
except:
    exitCode("DB Error")

###
class PhoneNumber(db.Model):
    __tablename__ = '_phoneNumbers'
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100), nullable=False)  # unique=True
    phone = db.Column("phonenumber", db.String(100),unique=True, nullable=False)

    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone

###

db.create_all()


@app.route("/")
def base():
    try:
        phone  = PhoneNumber("Mohammadjavhhad","+98234625235")
        db.session.add(phone)
        db.session.commit()
    except:
        pass
    return "ARVAN"

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


if __name__ == "__main__":
    app.run(debug=False)