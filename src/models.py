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
    is_active = Column(db.Boolean(False), nullable=False)
    users_room_relationship = db.relationship('Room', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "location": self.location,
        }

    @classmethod
    def read_by_user(cls, user_id):
        rooms_by_user = Room.query.filter_by(id_user = user_id)
        rooms_from_user = list(map(lambda x: x.serialize(), rooms_by_user))
        return rooms_from_user

    @classmethod
    def read_by_id(cls, room_id):
        room = Room.query.filter_by(id = room_id).first()
        return room

    def update_room(self, name_room):
        self.name_room = name_room
        db.session.commit()
        return self.serialize()

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_room = db.Column(db.String(20), unique=False, nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey("users.id"))
    room_Plants_relationship = db.relationship('Plants', lazy=True)

    def __repr__(self):
        return '<Room %r>' % self.name_room

    def serialize(self):
        return {
            "id": self.id,
            "name_room": self.name_room,
            "id_user": self.id_user
        }
    
    def create(self):
        db.session.add(self)
        db.session.commit()

class Plants_Type(db.Model):
    __tablename__ = "typeplant"
    id = db.Column(db.Integer, primary_key=True)
    name_type = db.Column(db.String(45), nullable=False)
    temperature_max_ideal = db.Column(db.Integer, nullable=False)
    temperature_min_ideal = db.Column(db.Integer, nullable=False)
    users_Plants_Type_relationship = db.relationship('Plants', lazy=True)

    def __repr__(self):
        return '<Plants_Type %r>' % self.name_type

    def serialize(self):
        return {
            "name_type": self.name_type,
            "temperature_max_ideal": self.temperature_max_ideal,
            "temperature_min_ideal": self.temperature_min_ideal
        }

class Plants_Grow_Phase(db.Model):
    __tablename__ = "growphaseplant"
    id = db.Column(db.Integer, primary_key=True)
    name_grow_phase = db.Column(db.String(45), nullable=False)
    humidity_max_ideal = db.Column(db.Integer, unique=False, nullable=False)
    humidity_min_ideal = db.Column(db.Integer, unique=False, nullable=False)
    users_Plants_Grow_Phase_relationship = db.relationship('Plants', lazy=True)

    def __repr__(self):
        return '<Plants_Grow_Phase %r>' % self.name_grow_phase

    def serialize(self):
        return {
            "name_grow_phase": self.name_grow_phase,
            "humdity_max_ideal": self.temperature_max_ideal,
            "humidity_min_ideal": self.temperature_min_ideal
        }

class Plants_Sensors(db.Model):
    __tablename__ = "sensorplant"
    id = db.Column(db.Integer, primary_key=True)
    sensor_number = db.Column(db.String(255),nullable=False)
    humidity_sensor = db.Column(db.Integer, unique=False, nullable=False)
    temperature_sensor = db.Column(db.Integer, unique=False, nullable=False)
    time_stamp = db.Column(db.Date, unique=False, nullable=False)
    users_sensor_relationship = db.relationship('Plants', lazy=True)

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

class Plants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_room = db.Column(db.Integer, db.ForeignKey("room.id"), nullable=False)
    name_plant = db.Column(db.String(45), nullable=False)
    type_plant = db.Column(db.Integer, db.ForeignKey("typeplant.id"), nullable=False)
    grow_phase = db.Column(db.Integer, db.ForeignKey("growphaseplant.id"), nullable=False)
    sensor_number = db.Column(db.Integer, db.ForeignKey("sensorplant.id"), nullable=False)


    def __repr__(self):
        return '<Plants %r>' % self.id_room

    def serialize(self):
        return {
            "id": self.id,
            "username_plant": self.name_plant,
            "type_plant": self.type_plant,
            "id_room": self.id_room
        }
    
    def create(self):
        db.session.add(self)
        db.session.commit() 