from datetime import datetime

from ..db import db

Respuesta = db.Table('Respuesta',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('alumno', db.Integer, db.ForeignKey('AlumnosTest.id'),nullable=False),
    db.Column('pregunta', db.Integer, db.ForeignKey('Pregunta.id'), nullable=False),
    db.Column('colegio', db.Integer, db.ForeignKey('Colegio.id'), nullable=False),
    db.Column('respuesta', db.Text))

PreguntasTest = db.Table('PreguntasTest',
    db.Column('id', db.Integer, primary_key=True, unique=True),
    db.Column('test', db.Integer, db.ForeignKey('Test.id'),nullable=False),
    db.Column('colegio', db.Integer, db.ForeignKey('Colegio.id'), nullable=False),
    db.Column('pregunta', db.Integer, db.ForeignKey('Pregunta.id'),nullable=False))

AlumnosTest = db.Table('AlumnosTest',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('test', db.Integer, db.ForeignKey('Test.id'),nullable=False),
    db.Column('colegio', db.Integer, db.ForeignKey('Colegio.id'), nullable=False),
    db.Column('alumno', db.Integer, db.ForeignKey('Alumno.id'), nullable=False),
    db.Column('respuesta', db.Integer, db.ForeignKey('Respuesta.id'), nullable=True))


class Test(db.Model):
    __tablename__='Test'
    id = db.Column(db.Integer, primary_key=True)
    estructura = db.Column(db.Integer, db.ForeignKey('TipoEstructura.id'), nullable=False)
    colegio = db.Column(db.Integer, db.ForeignKey('Colegio.id'), nullable=False)
    fecha_cierre = db.Column(db.DateTime, nullable=False)
    school_year = db.Column(db.Integer, nullable=False)
    first = db.Column(db.Integer,nullable=False)
    followUp = db.Column(db.Integer, nullable=True)
    final = db.Column(db.Integer, nullable=True)
    

    def __init__(self, estructura, colegio, fecha_cierre, school_year, followUp, final, first=None):
        self.estructura = estructura
        self.colegio = colegio
        self.fecha_cierre = fecha_cierre
        self.school_year = school_year
        self.followUp = followUp
        self.final = final
        self.first = first

    def __repr__(self):
        return '<Test %r>' % self.id

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'estructura': self.estructura,
            'colegio': self.colegio,
            'fecha_cierre': self.fecha_cierre,
            'school_year': self.school_year,
            'followUp': self.followUp,
            'first': self.first,
            'final': self.final
        }