from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    location = db.Column(db.String(30), unique=False, nullable=False)
    photo = db.Column(db.String(250), unique=False, nullable=True)
    users_room_relationship = db.relationship('Room', lazy=True)
    users_friends_relationship = db.relationship('Friends', lazy=True)
    
class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_room = db.Column(db.String(30), unique=False, nullable=False)
    id_user = db.Column(db.String(45), db.ForeignKey("users.username"),nullable=False)
    room_Plants_relationship = db.relationship('Plants', lazy=True)

class Plants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_plant = db.Column(db.String(45), unique=False, nullable=False)
    tipo_plant = db.Column(db.String(45), unique=True, nullable=False)
    id_room = db.Column(db.Integer, db.ForeignKey("room.id"), nullable=False)
    users_Plants_Tipo_relationship = db.relationship('Plants_Tipo', lazy=True)
    users_Plants_Time_relationship = db.relationship('Plants_Time', lazy=True)

class Plants_Tipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_tipo = db.Column(db.String(45), db.ForeignKey("plants.tipo_plant"), nullable=False)
    humidity_ideal = db.Column(db.Integer, unique=False, nullable=False)
    temperature_ideal = db.Column(db.Integer, unique=False, nullable=False)

class Plants_Time(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_stamp = db.Column(db.Integer, unique=False, nullable=False)
    humidity_sensor = db.Column(db.Integer, unique=False, nullable=False)
    temperature_sensor = db.Column(db.Integer, unique=False, nullable=False)
    sensor_name = db.Column(db.String(45), unique=False, nullable=False)
    id_plant_name = db.Column(db.Integer, db.ForeignKey("plants.id"),nullable=False)

class Friends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    friend_name = db.Column(db.String(45), unique=False, nullable=False)

    # def __repr__(self):
    #     return '<User %r>' % self.username

    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         "email": self.email,
    #         # do not serialize the password, its a security breach
    #     }