"""
API Endpoints NexaFemme
"""
from flask import Blueprint, request, jsonify
from api.models import db, User, CycleData, DailyLog, RelationshipLog
from api.utils import APIException
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
from datetime import datetime

api = Blueprint("api", __name__)
CORS(api)


# ---------------------------------------------------
# HELLO
# ---------------------------------------------------
@api.route("/hello")
def hello():
    return jsonify({"message": "Hola desde NexaFemme Backend"}), 200



# ===================================================
#  USER: REGISTER + LOGIN
# ===================================================

@api.route("/register", methods=["POST"])
def register():
    data = request.json
    nombre = data.get("nombre")
    email = data.get("email")
    password = data.get("password")

    if not nombre or not email or not password:
        raise APIException("Faltan datos", 400)

    existe = User.query.filter_by(email=email).first()
    if existe:
        raise APIException("El email ya está registrado", 400)

    nuevo = User(
        nombre=nombre,
        email=email,
        password_hash=generate_password_hash(password)
    )

    db.session.add(nuevo)
    db.session.commit()

    return jsonify(nuevo.serialize()), 201



@api.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()
    if not user:
        raise APIException("Usuario no encontrado", 404)

    if not check_password_hash(user.password_hash, password):
        raise APIException("Contraseña incorrecta", 401)

    return jsonify(user.serialize()), 200



# ===================================================
#  CICLO MENSTRUAL
# ===================================================

@api.route("/cycle/<int:user_id>", methods=["GET"])
def get_cycle(user_id):
    ciclo = CycleData.query.filter_by(user_id=user_id).first()
    if not ciclo:
        return jsonify({"msg": "No hay datos del ciclo"}), 404

    return jsonify(ciclo.serialize()), 200


@api.route("/cycle/<int:user_id>", methods=["POST"])
def create_or_update_cycle(user_id):
    data = request.json
    
    ciclo = CycleData.query.filter_by(user_id=user_id).first()

    if ciclo:
        # UPDATE
        ciclo.ultimo_periodo = datetime.strptime(data["ultimo_periodo"], "%Y-%m-%d")
        ciclo.duracion_ciclo = data["duracion_ciclo"]
        ciclo.duracion_menstruacion = data["duracion_menstruacion"]
    else:
        # CREATE
        ciclo = CycleData(
            user_id=user_id,
            ultimo_periodo=datetime.strptime(data["ultimo_periodo"], "%Y-%m-%d"),
            duracion_ciclo=data["duracion_ciclo"],
            duracion_menstruacion=data["duracion_menstruacion"]
        )
        db.session.add(ciclo)

    db.session.commit()
    return jsonify(ciclo.serialize()), 200



# ===================================================
#  DAILY LOG
# ===================================================

@api.route("/daily/<int:user_id>", methods=["GET"])
def get_daily_logs(user_id):
    logs = DailyLog.query.filter_by(user_id=user_id).all()
    return jsonify([l.serialize() for l in logs]), 200


@api.route("/daily/<int:user_id>", methods=["POST"])
def create_daily_log(user_id):
    data = request.json

    log = DailyLog(
        user_id=user_id,
        fecha=datetime.strptime(data["fecha"], "%Y-%m-%d"),
        sueno_horas=data.get("sueno_horas"),
        estres_nivel=data.get("estres_nivel"),
        energia_nivel=data.get("energia_nivel"),
        humor=data.get("humor"),
        entreno_tipo=data.get("entreno_tipo"),
        entreno_intensidad=data.get("entreno_intensidad"),
        notas=data.get("notas")
    )

    db.session.add(log)
    db.session.commit()

    return jsonify(log.serialize()), 201



# ===================================================
#  RELATIONSHIP LOG
# ===================================================

@api.route("/relationship/<int:user_id>", methods=["GET"])
def get_relationship_logs(user_id):
    logs = RelationshipLog.query.filter_by(user_id=user_id).all()
    return jsonify([l.serialize() for l in logs]), 200


@api.route("/relationship/<int:user_id>", methods=["POST"])
def create_relationship_log(user_id):
    data = request.json

    log = RelationshipLog(
        user_id=user_id,
        fecha=datetime.strptime(data["fecha"], "%Y-%m-%d"),
        tipo_relacion=data.get("tipo_relacion"),
        clima=data.get("clima"),
        notas=data.get("notas")
    )

    db.session.add(log)
    db.session.commit()

    return jsonify(log.serialize()), 201
