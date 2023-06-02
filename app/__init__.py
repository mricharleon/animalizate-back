from pyramid import events
from pyramid.config import Configurator
from pyramid.response import Response
from .sqlalchemy import configure_sqlalchemy, create_session, text

test=None


def hello_world(request):
    return Response('<body><h1>Hello World!</h1></body>')


def on_new_request(event):
    # metodo para setear el esquema, de acuerdo a la info del token
    # en el token viene en sub del usuario y se consultaria en initdb el esquema
    # schema_name = _figire_out_schema_name_from_request(event.request)
    session = create_session(test)
    event.request.dbsession = session
    schema_name = 'init'
    session.execute(text("SET search_path TO %s" % schema_name))

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    config = Configurator(settings=settings)

    # Configurar SQLAlchemy
    session_factory = configure_sqlalchemy(settings)
    config.registry['dbsession_factory'] = session_factory
    global test
    test = session_factory


    config.include('.routes.global')
    config.include('.models')
    config.scan('.views.views')

    config.add_subscriber(on_new_request, events.NewRequest)
    return config.make_wsgi_app()
