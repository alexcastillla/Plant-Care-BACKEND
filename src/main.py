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

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/<int:user_id>/rooms/<int:room_id>/plants/<int:plant_id>' , methods=['PATCH'])
def update_plant(user_id, room_id, plant_id):
    body = request.get_json()
    if body is None:
        raise APIException("You need to specify the request body as a json object", status_code=400)
    if 'name_plant' not in body:
        raise APIException('You need to specify the name of the plant', status_code=400)
    if 'type_plant' not in body:
        raise APIException('You need to specify the type of plant', status_code=400)
    if 'grow_phase' not in body:
        raise APIException('You need to specify the grow phase', status_code=400)
    plant_to_update = Plants.read_by_id_single_plant(plant_id, room_id)
    plant_updated =  plant_to_update.update_plant(id_room=body['id_room'], name_plant=body["name_plant"], type_plant=body["type_plant"], grow_phase=body["grow_phase"], sensor_number=body["sensor_number"])
    return jsonify(plant_updated), 200

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
