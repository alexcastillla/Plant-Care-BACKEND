data = {
    "Users": [
        {
        "id" : 1,
        "username": "alexcastilla"
        "email": "alexcastillla@gmail.com",
        "password": "c1234567",
        "location" : "Valencia",
        "photo" : None,
        },
        {
        "id" : 2,
        "username": "aurealianvoinea"
        "email": "aurelianvoinea@gmail.com",
        "password": "a1234567",
        "location" : "Madrid",
        "photo" : None,
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
    "Plants": [
        {
        "id": 1,
        "id_room": 1,
        "name_plant": "Rosita",
        "tipo_plant": "Interior",
        "grow_phase": "Crecimiento",
        "sensor_number": 111,
        },
        {
        "id": 2,
        "id_room": 1,
        "name_plant": "Cactus",
        "tipo_plant": "Exterior",
        "grow_phase": "Maduración",
        "sensor_number": 112,
        },
        {
        "id": 3,
        "id_room": 2,
        "name_plant": "Pepino",
        "tipo_plant": "Interior",
        "grow_phase": "Crecimiento",
        "sensor_number": 113,
        },
        {
        "id": 4,
        "id_room": 3,
        "name_plant": "Groot Madre",
        "tipo_plant": "Interior",
        "grow_phase": "Germinación",
        "sensor_number": 114,
        },
        {
        "id": 5,
        "id_room": 3,
        "name_plant": "Groot Padre",
        "tipo_plant": "Interior",
        "grow_phase": "Germinación",
        "sensor_number": 115,
        }
    ],
    "Plants_Tipo": [
        {
        "id": 1,
        "name_tipo": "Exterior",
        "temperature_max_ideal": 3,
        "temperature_min_ideal": 38,
        },
        {
        "id": 2,
        "name_tipo": "Interior",
        "temperature_max_ideal": 24,
        "temperature_min_ideal": 10,
        }
    ],
    "Plants_Grow_Phase": [
        {
        "id": 1,
        "name_tipo": "Germinación",
        "humidity_max_ideal": 0.85,
        "humidity_min_ideal": 0.80,
        },
        {
        "id": 2,
        "name_tipo": "Crecimiento",
        "humidity_max_ideal": 0.70,
        "humidity_min_ideal": 0.60,
        },
        {
        "id": 3,
        "name_tipo": "Maduración",
        "humidity_max_ideal": 0.50,
        "humidity_min_ideal": 0.20,
        }    
    ],
    "Plants_Sensors": [
        {
        "id": 1,
        "sensor_number": 111,
        "time_stamp": "2020-11-11 12:34:5",
        "humidity_sensor": 0.5,
        "temperature_sensor": 15,
        },
        {
        "id": 2,
        "sensor_number": 112,
        "time_stamp": "2020-11-11 12:34:5",
        "humidity_sensor": 0.6,
        "temperature_sensor": 13,
        },
        {
        "id": 3,
        "sensor_number": 113,
        "time_stamp": "2020-11-11 12:34:5",
        "humidity_sensor": 0.4,
        "temperature_sensor": 23,
        },
        {
        "id": 4,
        "sensor_number": 114,
        "time_stamp": "2020-11-11 12:34:5",
        "humidity_sensor": 0.8,
        "temperature_sensor": 22,
        },
        {
        "id": 5,
        "sensor_number": 115,
        "time_stamp": "2020-11-11 12:34:5",
        "humidity_sensor": 0.9,
        "temperature_sensor": 18,
        }
    ],