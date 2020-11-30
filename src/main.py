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

@app.route('/<int:user_id>/rooms', methods=['GET'])
def get_rooms(user_id):
    try:
        rooms = Room.read_by_user(user_id)
        return jsonify(rooms), 200
    except:
        return "Room not found", 400

@app.route('/<int:user_id>/rooms/<int:room_id>', methods=['PATCH'])
def update_room(user_id, room_id):
    body = request.get_json()
    if body is None:
        raise APIException("You need to specify the request body as a json object", status_code=400)

    room_to_update = Room.read_by_id(room_id)
    room_updated = room_to_update.update_room(body["name_room"])

    return jsonify(room_updated), 200

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
