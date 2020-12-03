from datetime import datetime

data = {
    "Users": [
        {
            "id" : 1,
            "username": "alexcastilla",
            "email": "alexcastillla@gmail.com",
            "password": "c1234567",
            "location" : "Valencia",
            "is_active": True,
        },
        {
            "id" : 2,
            "username": "aurealianvoinea",
            "email": "aurelianvoinea@gmail.com",
            "password": "a1234567",
            "location" : "Madrid",
            "is_active": True,
        }
    ],
    "Room": [
        {
            "id": 1,
            "id_user": 1,
            "name_room": "Terraza calle",
        },
        {
            "id": 2,
            "id_user": 1,
            "name_room": "Patio Mamá",
        },
        {
            "id": 3,
            "id_user": 2,
            "name_room": "Habitación Andrea",
        },
    ],
    "Plants_Type": [
        {
            "id": 1,
            "name_type": "Exterior",
            "temperature_max_ideal": 3,
            "temperature_min_ideal": 38,
        },
        {
            "id": 2,
            "name_type": "Interior",
            "temperature_max_ideal": 24,
            "temperature_min_ideal": 10,
        }
    ],
    "Plants_Grow_Phase": [
        {
            "id": 1,
            "name_grow_phase": "Germinacion",
            "humidity_max_ideal": 0.85,
            "humidity_min_ideal": 0.80,
        },
        {
            "id": 2,
            "name_grow_phase": "Crecimiento",
            "humidity_max_ideal": 0.70,
            "humidity_min_ideal": 0.60,
        },
        {
            "id": 3,
            "name_grow_phase": "Maduracion",
            "humidity_max_ideal": 0.50,
            "humidity_min_ideal": 0.20,
        }    
    ],
    "Plants_Sensors": [
        {
            "id": 1,
            "sensor_number": 111,
            "time_stamp": datetime.now(),
            "humidity_sensor": 0.5,
            "temperature_sensor": 15,
        },
        {
            "id": 2,
            "sensor_number": "112",
            "time_stamp": datetime.now(),
            "humidity_sensor": 0.6,
            "temperature_sensor": 13,
        },
        {
            "id": 3,
            "sensor_number": "113",
            "time_stamp": datetime.now(),
            "humidity_sensor": 0.4,
            "temperature_sensor": 23,
        },
        {
            "id": 4,
            "sensor_number": "114",
            "time_stamp": datetime.now(),
            "humidity_sensor": 0.8,
            "temperature_sensor": 22,
        },
        {
            "id": 5,
            "sensor_number": "115",
            "time_stamp": datetime.now(),
            "humidity_sensor": 0.9,
            "temperature_sensor": 18,
        },
    ],
    "Plants": [
        {
            "id": 1,
            "id_room": 1,
            "name_plant": "Rosita",
            "type_plant": 2,
            "grow_phase": 2,
            "sensor_number": 1,
        },
        {
            "id": 2,
            "id_room": 1,
            "name_plant": "Cactus",
            "type_plant": 1,
            "grow_phase": 3,
            "sensor_number": 2,
        },
        {
            "id": 3,
            "id_room": 2,
            "name_plant": "Pepino",
            "type_plant": 2,
            "grow_phase": 2,
            "sensor_number": 3,
        },
        {
            "id": 4,
            "id_room": 3,
            "name_plant": "Groot Madre",
            "type_plant": 2,
            "grow_phase": 1,
            "sensor_number": 4,
        },
        {
            "id": 5,
            "id_room": 3,
            "name_plant": "Groot Padre",
            "type_plant": 2,
            "grow_phase": 1,
            "sensor_number": 5,
        }
    ]
}