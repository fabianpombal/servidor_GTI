from ..db import db  

class TipoEdad(db.Model):
    __tablename__ = 'TipoEdad'
    id = db.Column(db.Integer, nullable=False, primary_key=True, unique=True)
    colegio = db.Column(db.Integer, db.ForeignKey('Colegio.id'), nullable=False)
    tipo_edad = db.Column(db.String(45), nullable=False, unique=True)
    franja_edad = db.Column(db.String(45), nullable=False)

    def __init__(self, colegio, tipo_edad, franja_edad):
        self.colegio = colegio
        self.tipo_edad = tipo_edad
        self.franja_edad = franja_edad

    def __repr__(self):
        return f'<TipoEdad {self.id}>'

    @property
    def serialize(self):
        return {
            'id': self.id,
            'colegio': self.colegio,
            'tipo': self.tipo_edad,
            'franja': self.franja_edad
        }
