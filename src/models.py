from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Boolean, Text, Float, Table, Date
from datetime import datetime

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    location = db.Column(db.String(30), unique=False, nullable=False)
    photo = db.Column(db.String(450), unique=False, nullable=True)
    users_room_relationship = db.relationship('Room', lazy=True)
    # users_friends_relationship = db.relationship('Friends', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "location": self.location,
            "photo": self.photo
        }
    
class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_room = db.Column(db.String(20), unique=False, nullable=False)
    id_user = db.Column(db.String(45), db.ForeignKey("users.username"))
    room_Plants_relationship = db.relationship('Plants', lazy=True)

    def __repr__(self):
        return '<Room %r>' % self.name_room

    def serialize(self):
        return {
            "id": self.id,
            "name_room": self.name_room,
            "id_user": self.id_user
        }

class Plants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_room = db.Column(db.Integer, db.ForeignKey("room.id"), nullable=False, primary_key=True)
    name_plant = db.Column(db.String(45), unique=False, nullable=False)
    tipo_plant = db.Column(db.Enum("Interior", "Exterior"), unique=False, nullable=False)
    grow_phase = db.Column(db.Enum("Germinación", "Crecimiento", "Maduración"), unique=True, nullable=False)
    sensor_number = db.Column(db.Integer, unique=True, nullable=False)
    users_Plants_Tipo_relationship = db.relationship('Plants_Tipo', lazy=True)
    users_Plants_Grow_Phase_relationship = db.relationship('Plants_Grow_Phase', lazy=True)
    users_Plants_Sensors_relationship = db.relationship('Plants_Sensors', lazy=True)
    users_sensor_relationship = db.relationship('Plants_Sensors', lazy=True)

    def __repr__(self):
        return '<Plants %r>' % self.id_room

    def serialize(self):
        return {
            "id": self.id,
            "username_plant": self.name_plant,
            "tipo_plant": self.tipo_plant,
            "id_room": self.id_room
        }

class Plants_Tipo(db.Model):
    name_tipo = db.Column(db.String(45), db.ForeignKey("plants.tipo_plant"), nullable=False, primary_key=True)
    temperature_max_ideal = db.Column(db.Integer, unique=False, nullable=False)
    temperature_min_ideal = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<Plants_Tipo %r>' % self.name_tipo

    def serialize(self):
        return {
            "name_tipo": self.name_tipo,
            "temperature_max_ideal": self.temperature_max_ideal,
            "temperature_min_ideal": self.temperature_min_ideal
        }

class Plants_Grow_Phase(db.Model):
    name_grow_phase = db.Column(db.String(45), db.ForeignKey("plants.grow_phase"), nullable=False, primary_key=True)
    humidity_max_ideal = db.Column(db.Integer, unique=False, nullable=False)
    humidity_min_ideal = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<Plants_Grow_Phase %r>' % self.name_grow_phase

    def serialize(self):
        return {
            "name_grow_phase": self.name_grow_phase,
            "humdity_max_ideal": self.temperature_max_ideal,
            "humidity_min_ideal": self.temperature_min_ideal
        }

class Plants_Sensors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sensor_number = db.Column(db.Integer, db.ForeignKey("plants.sensor_number"),nullable=False, primary_key=True)
    humidity_sensor = db.Column(db.Integer, unique=False, nullable=False)
    temperature_sensor = db.Column(db.Integer, unique=False, nullable=False)
    time_stamp = db.Column(db.Date, unique=False, nullable=False)

    def __repr__(self):
        return '<Plants_Sensors %r>' % self.sensor_number

    def serialize(self):
        return {
            "id": self.id,
            "sensor_number": self.sensor_number,
            "humidity_sensor": self.humidity_sensor,
            "temperature_sensor": self.temperature_sensor,
            "time_stamp": self.time_stamp
        }

# class Friends(db.Model):
#     follower = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
#     followed = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)

#     def __repr__(self):
#         return '<Friends %r>' % self.follower

#     def serialize(self):
#         return {
#             "id": self.id,
#             "follower": self.follower,
#             "followed": self.followed
#         }