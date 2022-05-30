"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
import json
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Favorite, Planets
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints

@app.route('/')
def sitemap():
    return generate_sitemap(app)

# hello API

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response"
    }
    return jsonify(response_body)


# Listar todos los usuarios del blog

@app.route('/user', methods=['GET'])
def list_users():
    user = User.query.all()
    userList_serialized = [userList.serialize() for userList in user]

    return jsonify({'response': userList_serialized})

#listar un solo user
@app.route('/user/<int:id_user>', methods=['GET'])
def get_user(id_user):
    user = User.query.filter_by(id=id_user).first()
    user = User.query.get(id_user)
    return jsonify(user.serialize()), 200

# Agregar usuarios

@app.route("/user", methods=['POST']) # aquí especificamos que estos endpoints aceptan solicitudes POST y GET.
def add_user():
    request_data = request.data
    data = json.loads(request_data)
    user.append(data)
    return jsonify({"msg" : "Usuario creado correctamente"})

# Borrar user

@app.route('/user/<int:id_user>', methods=['DELETE'])
def delete_user(id_user):
    user.pop(id_user)
    return jsonify({"msg" : "Usuario eliminado correctamente"})

#Listar la información de los favoritos

@app.route('/favorite', methods=['GET'])
def list_favorite():
    favorite = Favorite.query.all()
    fav_serialized = [fav.serialize() for fav in favorite]

    return jsonify({'response':fav_serialized})

#Listar la información de todos los planetas

@app.route('/planets', methods=['GET'])
def get_all_planets():
    planets = Planets.query.all()
  # planets_serialized = list(map(lambda planets:planets.serialize(), planets))
    planets_serialized = [planet.serialize() for planet in planets]

    return jsonify({'response':planets_serialized})

#Listar la información de un solo planet

@app.route('/planets/<int:id_planets>', methods=['GET'])
def get_planets(id_planets):
    planet = Planets.query.filter_by(id=id_planets).first()
    planet = Planets.query.get(id_planets)
    return jsonify(planet.serialize()), 200




# this only runs if `$ python src/main.py` is executed

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)





   # planet = {}
   # for planet in planets:
    #    if item.get(id) == id_planets:
     #       planet = item
    #return jsonify(palnet)
