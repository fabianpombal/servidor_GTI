from ..db import db 

class TipoPregunta(db.Model):
    __tablename__ = 'TipoPregunta'
    id = db.Column(db.Integer, nullable=False, primary_key=True, unique=True)
    tipo = db.Column(db.String(3), nullable=False, unique=True)
    colegio = db.Column(db.Integer, db.ForeignKey('Colegio.id'), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)

    def __init__(self, tipo, descripcion, colegio) -> None:
        self.tipo = tipo
        self.descripcion = descripcion
        self.colegio = colegio
    
    def __repr__(self) -> str:
        return '<TipoPregunta %r>'%self.id
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'tipo': self.tipo,
            'descripcion': self.descripcion,
            'colegio': self.colegio
        }