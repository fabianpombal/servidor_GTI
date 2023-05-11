from sqlalchemy import UniqueConstraint

from ..db import db
from flask_bcrypt import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ ='User'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    apellidos = db.Column(db.String(255), nullable=False)
    dni = db.Column(db.String(9), nullable=True)
    colegio = db.Column(db.Integer, db.ForeignKey('Colegio.id'),
                        nullable=False)
    rol = db.Column(db.Integer, db.ForeignKey('Rol.id'),
                    nullable=False)
    password = db.Column(db.String(255), nullable=True)
    activo = db.Column(db.Integer, nullable=False)


    def __init__(self, colegio, rol, nombre, apellidos, password, activo):
        self.colegio = colegio
        self.rol = rol
        self.activo = activo
        self.nombre = nombre
        self.apellidos = apellidos
        self.password = password


    def __repr__(self):
        return '<User %r>' % self.id

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellidos': self.apellidos,
            'colegio': self.colegio,
            'rol': self.rol,
            'activo': self.activo,
            'password': self.password
        }