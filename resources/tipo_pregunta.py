import sys

from flask import Response, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError

from database import db

from database.models.tipo_pregunta import TipoPregunta


from flask_restful import Resource

from resources.errors import SchemaValidationError, InternalServerError, TipoPreguntaNotExistsError, TipoPreguntaAlreadyExistsError
from datetime import datetime
# from resources.decorators import profesor, superuser, alumno

class TipoPreguntasApi(Resource):

    def get(self):
        try:
            db.openSession()
            tipoPreguntas = TipoPregunta.query.all()
            db.session.close()
            return jsonify(tipoPreguntas=[i.serialize for i in tipoPreguntas])
        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
            raise InternalServerError
    
    def post(self):
        try:
            body = request.get_json()
            tipoPregunta = TipoPregunta(**body)
            db.openSession()
            db.session.add(tipoPregunta)
            db.session.commit()
            id = tipoPregunta.id

            db.session.close()
            return {'id': str(id)}, 200
        except IntegrityError:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
            raise TipoPreguntaAlreadyExistsError
        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
            raise InternalServerError
    

class TipoPreguntaApi(Resource):
    def get(self, id):
        try:
            db.openSession()
            tipoPregunta = TipoPregunta.query.get(id)
            db.session.close()
            return jsonify(tipoPregunta.serialize)
        except AttributeError:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
            raise TipoPreguntaNotExistsError
        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
            raise InternalServerError
    
    def delete(self, id):
        try:
            db.openSession()
            db.session.query(TipoPregunta).filter_by(id=id).delete()
            db.session.commit()
            db.session.close()
            return '', 200
        except AttributeError:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
            raise TipoPreguntaNotExistsError
        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
            raise InternalServerError
    
    def put(self, id):
        try:
            db.openSession()
            tipoPregunta = db.session.query(TipoPregunta).filter(TipoPregunta.id == id).one()
            body = request.get_json()
            for key, value in body.items():
                setattr(tipoPregunta, key, value)
            db.session.commit()
            db.session.close()
        except AttributeError:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
            raise TipoPreguntaNotExistsError
        except IntegrityError:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
            raise TipoPreguntaAlreadyExistsError
        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
            raise InternalServerError