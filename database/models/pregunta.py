from ..db import db 

class Pregunta(db.Model):
    __tablename__ = 'Pregunta'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    pregunta = db.Column(db.Text, nullable=True)
    tipo_estructura = db.Column(db.Integer, db.ForeignKey('TipoEstructura.id'), nullable=False)
    tipo_pregunta = db.Column(db.Integer, db.ForeignKey('TipoPregunta.id'), nullable=False)
    tipo_edad = db.Column(db.Integer, db.ForeignKey('TipoEdad.id'), nullable=False)
    colegio = db.Column(db.Integer, db.ForeignKey('Colegio.id'), nullable=False)
    
    def __init__(self, pregunta, tipo_estructura, tipo_pregunta, tipo_edad,colegio):
        self.pregunta = pregunta
        self.tipo_estructura = tipo_estructura
        self.tipo_pregunta = tipo_pregunta
        self.tipo_edad = tipo_edad
        self.colegio = colegio

    def __repr__(self):
        return '<Pregunta %r>' % self.id

    @property
    def serialize(self):
        return {
            'id': self.id,
            'pregunta': self.pregunta,
            'tipo_pregunta': self.tipo_pregunta,
            'tipo_estructura': self.tipo_estructura,
            'tipo_edad': self.tipo_edad,
            'colegio': self.colegio
            
        }