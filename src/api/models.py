from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    # Relación con ciclo
    cycle = db.relationship("CycleData", backref="user", uselist=False)

    # Relación con logs diarios
    daily_logs = db.relationship("DailyLog", backref="user", lazy=True)

    # Relación con relaciones
    relationships = db.relationship("RelationshipLog", backref="user", lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email
        }


class CycleData(db.Model):
    __tablename__ = "cycle_data"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    ultimo_periodo = db.Column(db.Date)
    duracion_ciclo = db.Column(db.Integer)
    duracion_menstruacion = db.Column(db.Integer)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "ultimo_periodo": self.ultimo_periodo,
            "duracion_ciclo": self.duracion_ciclo,
            "duracion_menstruacion": self.duracion_menstruacion,
        }


class DailyLog(db.Model):
    __tablename__ = "daily_log"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    fecha = db.Column(db.Date)
    sueno_horas = db.Column(db.Integer)
    estres_nivel = db.Column(db.Integer)
    energia_nivel = db.Column(db.Integer)
    humor = db.Column(db.String(50))
    entreno_tipo = db.Column(db.String(50))
    entreno_intensidad = db.Column(db.String(50))
    notas = db.Column(db.Text)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "fecha": self.fecha,
            "sueno_horas": self.sueno_horas,
            "estres_nivel": self.estres_nivel,
            "energia_nivel": self.energia_nivel,
            "humor": self.humor,
            "entreno_tipo": self.entreno_tipo,
            "entreno_intensidad": self.entreno_intensidad,
            "notas": self.notas
        }


class RelationshipLog(db.Model):
    __tablename__ = "relationship_log"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    fecha = db.Column(db.Date)
    tipo_relacion = db.Column(db.String(80))
    clima = db.Column(db.String(80))
    notas = db.Column(db.Text)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "fecha": self.fecha,
            "tipo_relacion": self.tipo_relacion,
            "clima": self.clima,
            "notas": self.notas
        }
