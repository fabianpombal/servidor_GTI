from flask import request, Flask
from flask_babel import Babel
from app import babel


from resources.colegio import ColegioApi, ColegiosApi
from resources.alumno import AlumnosApi
from resources.test import TestsApi
from resources.tipo_estructura import TipoEstructurasApi
from resources.tipo_pregunta import TipoPreguntasApi
from resources. tipo_edad import TipoEdadesApi




def initialize_routes(api, jwt):
    
    def get_locale():
        body = request.get_json(silent=True)
        if body:
            if 'idioma' in body:
                lang = int(body['idioma'])
            else:
                lang = -1
        elif 'idioma' in request.args:
            lang = int(request.args.get('idioma'))
        else:
            lang = -1
        if lang == 0:
            return 'es'
        elif lang == 1:
            return 'gl'
        elif lang == 2:
            return 'en'
        else:
            return 'es'
    app = Flask(__name__)
    babel = Babel(app, locale_selector=get_locale)


    # metodo de consulta de colegios GET y POST
    api.add_resource(ColegiosApi, '/colegios')
    # metodo de consulta un colegio GET / DELETE / PUT
    api.add_resource(ColegioApi, '/colegio/<id>')
    #metodo de consulta de alumnos
    api.add_resource(AlumnosApi, '/alumnos')
    #metodo de consulta de tests GET y POST
    api.add_resource(TestsApi, '/tests')
    api.add_resource(TipoEstructurasApi, '/tipo_estructuras')
    api.add_resource(TipoEdadesApi, '/tipo_edades')
    api.add_resource(TipoPreguntasApi, '/tipo_preguntas')


  


