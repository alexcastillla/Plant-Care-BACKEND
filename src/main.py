"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, make_response
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap, token_required
from admin import setup_admin
from models import db, Users
from init_database import init_db
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
import datetime

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


@app.route('/register', methods=['GET', 'POST'])
def signup_user():  
 data = request.get_json()  

 hashed_password = generate_password_hash(data['password'], method='sha256')
 
 new_user = Users(username=data['username'], email=data['email'], password=hashed_password, location=data['location'], is_active=True) 
 new_user.create_user()

 
 

 return jsonify({'message': 'registered successfully'})

@app.route('/login', methods=['POST'])
def login_user():
    body = request.get_json()
    
    if "x-acces-tokens" not in request.headers:
        if not body or not body["email"] or not body["password"]:
            return "El email o la contraseña no son correctas", 401
      
        user = Users.read_user_by_mail(body["email"])
        print(user)
    
        if check_password_hash(user.password, body["password"]):
            token = jwt.encode({'id': user.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
            return jsonify({'token' : token.decode('UTF-8')}, 200)
        
        return "Password Invalid", 400
    
    else:
        return "Token válido", 200

@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    result = []

    for user in users:
        user_data = {}
        user_data['email'] = user.email  
        user_data['password'] = user.password

        result.append(user_data)
        return jsonify({'users': result})




if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
