import sys

from flask import Response, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError

from database import db

from database.models.pregunta import Pregunta


from flask_restful import Resource

from resources.errors import SchemaValidationError, InternalServerError, PreguntaNotExistsError, PreguntaAlreadyExistsError
from datetime import datetime
# from resources.decorators import profesor, superuser, alumno

class PreguntasApi(Resource):

    def get(self):
        try:
            db.openSession()
            preguntas = Pregunta.query.all()
            db.session.close()
            return jsonify(preguntas=[i.serialize for i in preguntas])
        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
            raise InternalServerError
    

    def post(self):
        try:
            db.openSession()
            body = request.get_json()
            pregunta = Pregunta(**body)
            db.session.add(pregunta)
            db.session.commit()
            id = test.id
            db.session.close()
           
            return {
                'id': str(id)
            }, 200
        except IntegrityError:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
            raise PreguntaAlreadyExistsError
        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
            raise InternalServerError

