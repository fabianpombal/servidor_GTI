from sqlalchemy import and_, UniqueConstraint

from ..db import db
from flask_babel import gettext

class Alumno(db.Model):
    __tablename__='Alumno'
    id = db.Column(db.Integer, primary_key=True)
    sexo = db.Column(db.String(1), nullable=False)
    nombre = db.Column(db.String(255), nullable=False)
    activo = db.Column(db.Integer, default=1, nullable=False)
    

    def __init__(self, nombre, sexo, activo):
        self.sexo = sexo
        self.activo = activo
        self.nombre = nombre

    def __repr__(self):
        return '<Alumno %r>' % self.id
    
    @property
    def sexo_display(self):
        """Return the gender in string instead of letter"""
        if self.sexo == 'H':
            return gettext('Hombre')
        elif self.sexo == 'M':
            return gettext('Mujer')
        else:
            return ''


    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return{
            'id': self.id,
            'nombre': self.nombre,
            'sexo': self.sexo,
            'activo': self.activo
        }
    

    