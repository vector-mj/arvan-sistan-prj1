from flask import Flask, jsonify, request
app = Flask(__name__)


# @app.route("/")
# def helloWorld():
#   return "Hi"

@app.route('/phonenumber', methods=['GET'])
def getPhoneNumber():
  s = request.get_json()
  return s, 204

@app.route('/phonenumber', methods=['POST'])
def setPhoneNumber():
  s = request.get_json()
  return s, 204

@app.route('/phonenumber', methods=['PUT'])
def putPhoneNumber():
  s = request.get_json()
  return s, 204

@app.route('/phonenumber', methods=['DELETE'])
def delPhoneNumber():
  s = request.get_json()
  return s, 204