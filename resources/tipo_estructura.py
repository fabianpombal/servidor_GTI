import sys

from flask import Response, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError

from database import db

from database.models.tipo_estructura import TipoEstructura


from flask_restful import Resource

from resources.errors import SchemaValidationError, InternalServerError, TipoEstructuraNotExistsError, TipoEstructuraAlreadyExistsError
from datetime import datetime
# from resources.decorators import profesor, superuser, alumno

class TipoEstructurasApi(Resource):
    def get(self):
        try:
            db.openSession()
            tipoEstructuras = TipoEstructura.query.all()
            db.session.close()
            return jsonify(tipoEstructuras=[i.serialize for i in tipoEstructuras])
        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
            raise InternalServerError
    
    def post(self):
        try:
            body = request.get_json()
            if "colegio" not in body:
                print("No existe colegio")
            tipoEstructura = TipoEstructura(**body)
            db.openSession()
            db.session.add(tipoEstructura)
            db.session.commit()

            id = tipoEstructura.id
            db.session.close()
            
            return {'id': str(id)}, 200
        except IntegrityError:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
            raise TipoEstructuraAlreadyExistsError
        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
            raise InternalServerError
        
# class TipoEstructuraApi(Resource):
#     def put(self, id):
#         try:
#             db.openSession()
#             tipoEstructura = db.session.query(TipoEstructura).filter(TipoEstructura.id==id).one()
#             body = request.get_json() #coge el cuerpo de la peticion del cliente
#             for key, value in body.items():
#                 setattr(tipoEstructura, key, value)
#             db.session.commit()
#             db.session.close()
#         except AttributeError:
#             exc_type, exc_obj, exc_tb = sys.exc_info()
#             print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
#             raise TipoEstructuraNotExistsError
#         except IntegrityError:
#             exc_type, exc_obj, exc_tb = sys.exc_info()
#             print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
#             raise TipoEstructuraAlreadyExistsError
#         except Exception:
#             exc_type, exc_obj, exc_tb = sys.exc_info()
#             print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
#             raise InternalServerError
    
#     def delete(self, id):
#         try:
#             db.openSession()
#             db.session.query(TipoEstructura).filter_by(id=id).delete()
#             db.session.commit()
#             db.session.close()
#             return '', 200
#         except AttributeError:
#             exc_type, exc_obj, exc_tb = sys.exc_info()
#             print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
#             raise TipoEstructuraNotExistsError
#         except Exception:
#             exc_type, exc_obj, exc_tb = sys.exc_info()
#             print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
#             raise InternalServerError
        
#     def get(self, id):
#         try:
#             db.openSession()
#             tipoEstructura = TipoEstructura.query.get(id)
#             db.session.close()
#             return jsonify(tipoEstructura.serialize)
#         except AttributeError:
#             exc_type, exc_obj, exc_tb = sys.exc_info()
#             print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
#             raise TipoEstructuraNotExistsError
#         except Exception:
#             exc_type, exc_obj, exc_tb = sys.exc_info()
#             print(exc_type, exc_obj, exc_tb.tb_lineno, flush=True)
#             raise InternalServerError
