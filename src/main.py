"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db
from init_database import init_db

app = Flask(__name__)
app.app_context().push()
data_base = os.environ['DB_CONNECTION_STRING']

app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = data_base
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)

CORS(app)
setup_admin(app)
app.cli.add_command(init_db)

@app.route('/user/<int:user_id>/rooms', methods=['POST'])
def add_new_room(user_id):  
    body = request.get_json()
    if body is None:
        raise APIException("You need to specify the request body as a json object", status_code=400)
    if 'name_room' not in body:
        raise APIException('You need to specify the name room', status_code=400)

    new_room = Room(name_room=body['name_room'], id_user=body["id_user"])
    new_room.create()

    return jsonify({'status': 'OK', 'message': 'Room Added succesfully'}), 201

@app.route('/user/<int:user_id>/rooms', methods=['GET'])
def get_rooms(user_id):
    rooms = Room.read_by_user(user_id)
    if rooms is None:
        return "You need to specify the request room as a json object, is empty", 400
    return jsonify(rooms), 200

@app.route('/user/<int:user_id>/rooms/<int:room_id>', methods=['PATCH'])
def update_room(user_id, room_id):
    body = request.get_json()
    if body is None:
        return "You need to specify the request body as a json object", 400

    room_to_update = Room.read_by_id(room_id)
    room_updated = room_to_update.update_room(body["name_room"])

    return jsonify(room_updated), 200

@app.route('/user/<int:user_id>/rooms/<int:room_id>/plants', methods=['POST'])
def add_new_plant(user_id, room_id):  
    body = request.get_json()
    if body is None:
        raise APIException("You need to specify the request body as a json object", status_code=400)
    if 'id_room' not in body:
        raise APIException('You need to specify the id room', status_code=400)
    if 'name_plant' not in body:
        raise APIException('You need to specify the name of the plant', status_code=400)
    if 'type_plant' not in body:
        raise APIException('You need to specify the type of plant', status_code=400)
    if 'grow_phase' not in body:
        raise APIException('You need to specify the grow phase', status_code=400)

    new_plant = Plants(id_room=body['id_room'], name_plant=body["name_plant"], type_plant=body["type_plant"], grow_phase=body["grow_phase"], sensor_number=body["sensor_number"]) 
    new_plant.create()

    return jsonify({'status': 'OK', 'message': 'Plant Added succesfully'}), 201

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
