from ..db import db
from hashlib import md5

class Colegio(db.Model):
    __tablename__='Colegio'
    
    nombre = db.Column(db.String(255), unique=True, nullable=False)
    hash = db.Column(db.String(255), nullable=False, primary_key=True)

    

    def __init__(self, nombre, hash):
        self.nombre = nombre
        self.hash = hash
        

    def __repr__(self):
        return f'<Colegio>\n<Nombre {self.nombre}>\n <Hash {self.hash}>\n<Colegio/>' 

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'nombre': self.nombre,
            'hash': self.hash
        }
    
    
   
