import sys

from flask import Response, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError

from database import db
from database.models.alumno import Alumno

from flask_restful import Resource

from resources.errors import SchemaValidationError, InternalServerError, AlumnoNotExistsError, AlumnoAlreadyExistsError
from datetime import datetime
# from resources.decorators import profesor, superuser, alumno

class AlumnosApi(Resource):

    def get(self):
        try:
            db.openSession()
            alumnos = Alumno.query.all()
            db.session.close()
            return jsonify(alumnos=[i.serialize for i in alumnos])
        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
            raise InternalServerError
        
    def post(self):
        try:
            db.openSession()
            body = request.get_json()
            print(body["nombre"])
           
            alumno = Alumno(**body)
            
            db.session.add(alumno)
            db.session.commit()
            id = alumno.id

            db.session.close()
            return {'id': str(id)}, 200
        except IntegrityError:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
            raise AlumnoAlreadyExistsError
        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
            raise InternalServerError