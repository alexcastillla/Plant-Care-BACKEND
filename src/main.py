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

@app.route('/<int:user_id>/rooms/<int:room_id>/plants', methods=['GET'])
def get_plants(user_id, room_id):
    try:
        plants = Plants.read_by_id(room_id)
        return jsonify(plants), 200
    except:
        return "Plants not found in this room", 400

@app.route('/<int:user_id>/rooms/<int:room_id>/plants/<int:plant_id>', methods=['GET'])
def get_single_plant(user_id, room_id, plant_id):
    try:
        single_plant = Plants.read_by_id_single_plant(plant_id, room_id)
        return jsonify(single_plant), 200
    except:
        return "Plant not found", 400

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
