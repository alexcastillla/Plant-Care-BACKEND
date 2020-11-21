from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    location = db.Column(db.String(30), unique=False, nullable=False)
    photo = db.Column(db.String(255), unique=False, nullable=True)
    users_room_relationship = db.relationship('Room', lazy=True)
    users_friends_relationship = db.relationship('Friends', lazy=True)

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
    id_user = db.Column(db.String(45), db.ForeignKey("users.username"),nullable=False)
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
    name_plant = db.Column(db.String(45), unique=False, nullable=False)
    tipo_plant = db.Column(db.Enum("Interior", "Exterior"), unique=True, nullable=False)
    id_room = db.Column(db.Integer, db.ForeignKey("room.id"), nullable=False)
    users_Plants_Tipo_relationship = db.relationship('Plants_Tipo', lazy=True)
    users_Plants_Time_relationship = db.relationship('Plants_Time', lazy=True)

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
    id = db.Column(db.Integer, primary_key=True)
    name_tipo = db.Column(db.String(45), db.ForeignKey("plants.tipo_plant"), nullable=False)
    humidity_ideal = db.Column(db.Integer, unique=False, nullable=False)
    temperature_ideal = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<Plants_Tipo %r>' % self.name_tipo

    def serialize(self):
        return {
            "id": self.id,
            "name_tipo": self.name_tipo,
            "humidity_ideal": self.humidity_ideal,
            "temperature_ideal": self.temperature_ideal
        }

class Plants_Time(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_stamp = db.Column(db.Integer, unique=False, nullable=False)
    humidity_sensor = db.Column(db.Integer, unique=False, nullable=False)
    temperature_sensor = db.Column(db.Integer, unique=False, nullable=False)
    sensor_name = db.Column(db.String(45), unique=False, nullable=False)
    id_plant_name = db.Column(db.Integer, db.ForeignKey("plants.id"),nullable=False)

    def __repr__(self):
        return '<Plants_Time %r>' % self.id_plant_name

    def serialize(self):
        return {
            "id": self.id,
            "time_stamp": self.time_stamp,
            "humidity_sensor": self.humidity_sensor,
            "temperature_sensor": self.temperature_sensor,
            "sensor_name": self.sensor_name
        }

class Friends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    friend_name = db.Column(db.String(45), unique=False, nullable=False)

    def __repr__(self):
        return '<Friends %r>' % self.id_user

    def serialize(self):
        return {
            "id": self.id,
            "id_user": self.id_user,
            "friend_name": self.friend_name
        }