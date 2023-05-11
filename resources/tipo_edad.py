import sys

from flask import Response, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError

from database import db

from database.models.tipo_edad import TipoEdad


from flask_restful import Resource

from resources.errors import SchemaValidationError, InternalServerError, GrupoEdadNotExistsError, GrupoEdadAlreadyExistsError
from datetime import datetime
# from resources.decorators import profesor, superuser, alumno

class TipoEdadesApi(Resource):
    def get(self):
        try:
            db.openSession()
            tipoEdades = TipoEdad.query.all()
            db.session.close()
            return jsonify(tipoEdades=[i.serialize for i in tipoEdades])
        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
            raise InternalServerError
    
    def post(self):
        try:
          
            body = request.get_json()
            print(body)

            tipoEdades = TipoEdad(**body)
           

            db.openSession()
            
            print(tipoEdades)
            db.session.add(tipoEdades)


            db.session.commit()
        
            id = tipoEdades.id

           
            db.session.close()
            
            return {'id': str(id)}, 200
        
        except IntegrityError:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
            raise GrupoEdadAlreadyExistsError
        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
            raise InternalServerError