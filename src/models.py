from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Boolean, Text, Float, Table, Date
from datetime import datetime
from sqlalchemy.orm import backref

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    location = db.Column(db.String(30), unique=False, nullable=False)
    is_active = Column(db.Boolean(False), nullable=False)
    users_room_relationship = db.relationship('Room', lazy=True)
    users_plants_relationship = db.relationship('Plants', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "location": self.location,
        }

    def create_user(self):
        db.session.add(self)  
        db.session.commit() 

    def read_user_by_mail(user_email):
        user = Users.query.filter_by(email = user_email).first()
        return user

    def delete_room(self):
        db.session.delete(self)
        db.session.commit()

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_room = db.Column(db.String(20), unique=False, nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey("users.id"))
    room_Plants_relationship = db.relationship('Plants', lazy=True)
    room_Plants_relationship = db.relationship('Plants', back_populates="relationship_to_room", cascade="all, delete-orphan", passive_deletes=True)

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
    
    def delete_room(self):
        db.session.delete(self)
        db.session.commit()

class Plants_Type(db.Model):
    __tablename__ = "typeplant"
    id = db.Column(db.Integer, primary_key=True)
    name_type = db.Column(db.String(45), nullable=False)
    temperature_max_ideal = db.Column(db.Float, nullable=False)
    temperature_min_ideal = db.Column(db.Float, nullable=False)
    users_Plants_Type_relationship = db.relationship('Plants', lazy=True)

    def __repr__(self):
        return '<Plants_Type %r>' % self.name_type

    def serialize(self):
        return {
            "id": self.id,
            "name_type": self.name_type,
            "temperature_max_ideal": self.temperature_max_ideal,
            "temperature_min_ideal": self.temperature_min_ideal
        }
    
    def create(self):
        db.session.add(self)
        db.session.commit()
           
    @classmethod
    def read_all_type(cls):
        all_types = Plants_Type.query.all()
        all_types_serialized = list(map(lambda x: x.serialize(), all_types))
        return all_types_serialized


class Plants_Grow_Phase(db.Model):
    __tablename__ = "growphaseplant"
    id = db.Column(db.Integer, primary_key=True)
    name_grow_phase = db.Column(db.String(45), nullable=False)
    humidity_max_ideal = db.Column(db.Float, unique=False, nullable=False)
    humidity_min_ideal = db.Column(db.Float, unique=False, nullable=False)
    users_Plants_Grow_Phase_relationship = db.relationship('Plants', lazy=True)

    def __repr__(self):
        return '<Plants_Grow_Phase %r>' % self.name_grow_phase

    def serialize(self):
        return {
            "id": self.id,
            "name_grow_phase": self.name_grow_phase,
            "humdity_max_ideal": self.humidity_max_ideal,
            "humidity_min_ideal": self.humidity_min_ideal
        }
    
    def create(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def read_all_grow(cls):
        all_grows = Plants_Grow_Phase.query.all()
        all_grows_serialized = list(map(lambda x: x.serialize(), all_grows))
        return all_grows_serialized

class Plants_Sensors(db.Model):
    __tablename__ = "sensorplant"
    id = db.Column(db.Integer, primary_key=True)
    sensor_number = db.Column(db.String(255),nullable=False)
    humidity_sensor = db.Column(db.Float, unique=False, nullable=False)
    temperature_sensor = db.Column(db.Float, unique=False, nullable=False)
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
    
    def create(self):
        db.session.add(self)
        db.session.commit()

class Plants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_room = db.Column(db.Integer, db.ForeignKey("room.id", ondelete="CASCADE"), nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey("users.id"))
    name_plant = db.Column(db.String(45), nullable=False)
    type_plant = db.Column(db.Integer, db.ForeignKey("typeplant.id"), nullable=False)
    grow_phase = db.Column(db.Integer, db.ForeignKey("growphaseplant.id"), nullable=False)
    sensor_number = db.Column(db.Integer, db.ForeignKey("sensorplant.id"), nullable=False)
    relationship_to_room = db.relationship("Room", back_populates="room_Plants_relationship")

    def __repr__(self):
        return '<Plants %r>' % self.name_plant

    def serialize(self):
        type_plant = self.get_type_data()
        grow_plant = self.get_grow_data()
        sensor_plant = self.get_sensor_data()

        return {
            "id": self.id,
            "id_room": self.id_room,
            "username_plant": self.name_plant,
            "type_plant": type_plant.name_type,
            "temperature_max_ideal": type_plant.temperature_max_ideal,
            "temperature_min_ideal": type_plant.temperature_min_ideal,
            "humidity_max_ideal": grow_plant.humidity_max_ideal,
            "humidity_min_ideal": grow_plant.humidity_min_ideal,
            "humidity_sensor": sensor_plant.humidity_sensor,
            "temperature_sensor": sensor_plant.temperature_sensor,
            "time_stamp": sensor_plant.time_stamp,
        }
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def read_by_id(cls, room_id):
        plants_by_user = Plants.query.filter_by(id_room = room_id)
        plants_from_user = list(map(lambda x: x.serialize(), plants_by_user))
        return plants_from_user

    @classmethod
    def read_by_single_plant_to_update(cls,room_id, plant_id,user_id):
        plant = Plants.query.filter_by(id = plant_id, id_room = room_id).first()
        return plant

    @classmethod
    def read_by_user(cls, user_id):
        all_plants_by_user = Plants.query.filter_by(id_user = user_id)
        all_plants_from_user = list(map(lambda x: x.serialize(), all_plants_by_user))
        return all_plants_from_user

    @classmethod
    def read_by_id_single_plant(cls, plant_id, room_id):
        plant = Plants.query.filter_by(id = plant_id, id_room = room_id).first()
        single_plant = list(map(lambda x: x.serialize(), plant))
        return single_plant

    @classmethod
    def read_by_id(cls, plant_id):
        plant = cls.query.filter_by(id=plant_id).first()
        return plant

    def get_type_data(self):
        type_plant = Plants_Type.query.filter_by(id = self.type_plant).first()
        return type_plant

    def get_grow_data(self):
        grow_plant = Plants_Grow_Phase.query.filter_by(id = self.grow_phase).first()
        return grow_plant
    
    def get_sensor_data(self):
        sensor_plant = Plants_Sensors.query.filter_by(id = self.sensor_number).first()
        return sensor_plant
    
    def plant_to_delete(self):
        db.session.delete(self)
        db.session.commit()



 
