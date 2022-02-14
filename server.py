from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request, make_response

from os import getenv
from dotenv import load_dotenv
from sys import exit as exitCode
from werkzeug.routing import Rule
import sqlalchemy

# loading environments
load_dotenv()
env = [getenv("MYSQL_URI"), getenv("LABLE")]
if None in env:
    exitCode("Please set all environment")

# flask app with db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = env[0]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.url_map.strict_slashes = False
db = SQLAlchemy(app)
try:
    db.engine.execute("select 1")
except Exception as e:
    print(e)
    exitCode("DB Error")

###


class PhoneNumber(db.Model):
    __tablename__ = '_phoneNumbers'
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100), nullable=False)  # unique=True
    phone = db.Column("phonenumber", db.String(100),
                      unique=True, nullable=False)
    desc = db.Column("description", db.String(100),
                     unique=False, nullable=False)

    def __init__(self, name: str, phone: str, desc: str = "Empty"):
        self.name = name
        self.phone = phone
        self.desc = desc

###


@app.route("/")
def base():
    return make_response(jsonify(Arvan="~Sistan~"))


@app.route('/phonenumber', methods=['GET'])
@app.route('/phonenumber/<numberId>', methods=['GET'])
def getPhoneNumber(numberId: str = ""):
    if numberId:
        existingId = PhoneNumber.query.filter(
            PhoneNumber.id == numberId).first()
        if existingId:
            return make_response(jsonify(name=existingId.name, phone=existingId.phone), 200)
        else:
            return make_response(jsonify(status="INFO", msg="This id doesn't exist in database"))
    else:
        phones = PhoneNumber.query.all()
        if len(phones) == 0:
            return make_response(jsonify(status="INFO", length=0, msg="We don't have any record in database"), 200)
        return make_response(jsonify(length=len(phones), Result=[{"id": phone.id, "name": phone.name, "phone": phone.phone} for phone in phones]), 200)


@app.route('/phonenumber', methods=['POST'])
def setPhoneNumber():
    fields = list(request.json.keys())
    if not set(["name", "phone"]).issubset(fields):
        return make_response(jsonify(staus="ERR", msg="Please set 'name' and 'phone' in body and try again"))
    else:
        try:
            name = request.json["name"]
            phone = request.json["phone"]
            desc = request.json["description"]
            newNumber = PhoneNumber(name, phone, desc)
            db.session.add(newNumber)
            db.session.commit()
            return make_response(jsonify(staus="OK", msg="New record created successfully", name=name, phone=phone, desc=desc))
        except sqlalchemy.exc.IntegrityError as e:
            return make_response(jsonify(staus="ERR", msg="This phone number already exists in database"), 500)
        except:
            return make_response(jsonify(staus="ERR", msg="Please try again later"), 500)


@app.route('/phonenumber', methods=['PUT'])
@app.route('/phonenumber/<numberId>', methods=['PUT'])
def putPhoneNumber(numberId: str = ""):
    if numberId:
        existingId = PhoneNumber.query.filter(
            PhoneNumber.id == numberId).first()
        if not existingId:
            return make_response(jsonify(status="ERR", msg="This id doesn't exist in database"), 200)
        else:
            existingId.name = request.json["name"]
            existingId.phone = request.json["phone"]
            db.session.commit()
            return make_response(jsonify(status="OK", msg="Record updated successfully"), 200)
    else:
        return make_response(jsonify(status="ERR", msg="Please set record ID parameter"), 200)


@app.route('/phonenumber', methods=['DELETE'])
@app.route('/phonenumber/<numberId>', methods=['DELETE'])
def delPhoneNumber(numberId: str = ""):
    if numberId:
        existingId = PhoneNumber.query.filter(
            PhoneNumber.id == numberId).first()
        if existingId:
            PhoneNumber.query.filter(PhoneNumber.id == numberId).delete()
            db.session.commit()
            return make_response(jsonify(status="ERR", msg="Record removed successfully"), 200)
        else:
            return make_response(jsonify(status="ERR", msg="This record ID doesn't exists in database"), 200)
    else:
        return make_response(jsonify(status="ERR", msg="Please set record ID parameter"), 200)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return make_response(jsonify(msg="Not Found"),404)


if __name__ == "__main__":
    db.create_all()
    app.run(host="0.0.0.0",port=18080)
