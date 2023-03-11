#more concise way to code for CRUD & APIs from parizbyte, so starting new file instead of referencing notes so much

#all imports needed to run this, this includes imports from the other files zipped in the folder which are Cargo_CRUD, Spaceship_CRUD, Captain_CRUD, API_Login
from flask import Flask, jsonify, request
import API_Login
import Cargo_CRUD
import Spaceship_CRUD
import Captain_CRUD

app = Flask(__name__)

#---------------------------------------API'S for Cargo Table --------------------------------------------------------------------------


#this is for testing to make sure api works#            
@app.route('/', methods=['GET']) # default url without any routing as GET request
def home():
    return "<h3>Testing to see if this works</h3>"


@app.route('/api/cargo', methods=["GET"])
def get_cargo():
    cargo = Cargo_CRUD.get_cargo()
    return jsonify(cargo)


@app.route("/api/insert_cargo", methods=["POST"])
def insert_cargo():
    cargo_details = request.get_json()
    weight = cargo_details["weight"]
    cargotype = cargo_details["cargotype"]
    departure = cargo_details["departure"]
    arrival = cargo_details["arrival"]
    shipid = cargo_details["shipid"]
    result = Cargo_CRUD.insert_cargo(weight, cargotype, departure, arrival, shipid)
    return jsonify(result)


@app.route("/api/cargo<id>", methods=["PUT"])
def update_cargo(id):
    cargo_details = request.get_json()
    id = cargo_details["id"]
    weight = cargo_details["weight"]
    cargotype = cargo_details["cargotype"]
    departure = cargo_details["departure"]
    arrival = cargo_details["arrival"]
    shipid = cargo_details["shipid"]
    result = Cargo_CRUD.update_cargo(id, weight, cargotype, departure, arrival, shipid)
    return jsonify(result)


@app.route("/api/delete_cargo", methods=["DELETE"])
def delete_cargo(id):
    result = Cargo_CRUD.delete_cargo(id)
    return jsonify(result)


#---------------------------------------API'S for Spaceship Table --------------------------------------------------------------------------


@app.route('/api/spaceship', methods=["GET"])
def get_spaceships():
    spaceship = Spaceship_CRUD.get_spaceships()
    return jsonify(spaceship)


@app.route("/api/insert_spaceship", methods=["POST"])
def insert_spaceship():
    spaceship_details = request.get_json()
    maxweight = spaceship_details["maxweight"]
    captainid = spaceship_details["captainid"]
    result = Spaceship_CRUD.insert_spaceship(maxweight, captainid)
    return jsonify(result)


@app.route("/api/spaceship<id>", methods=["PUT"])
def update_spaceship(id):
    spaceship_details = request.get_json()
    id = spaceship_details["id"]
    maxweight = spaceship_details["maxweight"]
    captainid = spaceship_details["captainid"]
    result = Spaceship_CRUD.update_spaceship(id, maxweight, captainid)
    return jsonify(result)


@app.route("/api/delete_spaceship", methods=["DELETE"])
def delete_spaceship(id):
    result = Spaceship_CRUD.delete_spaceship(id)
    return jsonify(result)


#---------------------------------------API'S for Captain Table --------------------------------------------------------------------------


@app.route('/api/captain', methods=["GET"])
def get_captains():
    captain = Captain_CRUD.get_captains()
    return jsonify(captain)


@app.route("/api/insert_captain", methods=["POST"])
def insert_captain():
    captain_details = request.get_json()
    firstname = captain_details["firstname"]
    lastname = captain_details["lastname"]
    captainrank = captain_details["captainrank"]
    homeplanet = captain_details["homeplanet"]
    result = Captain_CRUD.insert_captain(firstname, lastname, captainrank, homeplanet)
    return jsonify(result)


@app.route("/api/captain<id>", methods=["PUT"])
def update_captain(id):
    captain_details = request.get_json()
    id = captain_details["id"]
    firstname = captain_details["firstname"]
    lastname = captain_details["lastname"]
    captainrank = captain_details["captainrank"]
    homeplanet = captain_details["homeplanet"]
    result = Captain_CRUD.update_captain(id,firstname, lastname, captainrank, homeplanet)
    return jsonify(result)


@app.route("/api/delete_captain", methods=["DELETE"])
def delete_captain(id):
    result = Captain_CRUD.delete_captain(id)
    return jsonify(result)


if __name__ == "__main__":

    

    app.run(host='', port=8000, debug=False)

#---------------------------------------SOURCES / REFERENCES----------------------------------------------
# table database & connection creation taken from Homework1
# https://www.geeksforgeeks.org/python-sqlite-crud-operations/
# https://dev.to/ayabouchiha/sending-get-post-put-delete-requests-in-python-45o8
# Some code is modeled after the example we did in class from the Notes (crudops nots, (crudops.py, sql.py,creds.py))
# API Tutorial https://www.youtube.com/watch?v=GMppyAPbLYk
# Code is largely modeled after this example & helped me understand better  https://parzibyte.me/blog/en/2020/11/12/creating-api-rest-with-python-flask-sqlite3/
#https://www.youtube.com/watch?v=CLG0ha_a0q8