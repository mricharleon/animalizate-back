from pyramid import events
from pyramid.config import Configurator
from pyramid.response import Response
import transaction
from sqlalchemy import text
from .sqlalchemy import configure_sqlalchemy, create_session



def hello_world(request):
    return Response('<body><h1>Hello World!</h1></body>')

def manager_hook(request):
    return transaction.TransactionManager(explicit=True)

def on_new_request(event):
    # metodo para setear el esquema, de acuerdo a la info del token
    # en el token viene en sub del usuario y se consultaria en initdb el esquema
    # schema_name = _figire_out_schema_name_from_request(event.request)
    dbsession = create_session(event)
    event.request.dbsession = dbsession

    schema_name = 'init'
    event.request.dbsession.execute(text("SET search_path TO %s" % schema_name))

def on_new_response(event):
    print('Sesion cerrada!')
    if hasattr(event.request, 'dbsession'):
        event.request.dbsession.close()
        event.request.dbsession.get_bind().dispose()
    else:
        print('No existe dbsession en request!')

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    settings['tm.manager_hook'] = manager_hook

    config = Configurator(settings=settings)

    # Configurar SQLAlchemy
    session_factory = configure_sqlalchemy(settings)
    config.registry['dbsession_factory'] = session_factory

    # para manejo de cierres automaticos de sessiones
    config.include('pyramid_retry')
    config.include('pyramid_tm')

    config.include('.routes.global')
    config.include('.models')
    config.scan('.views.views')

    config.add_subscriber(on_new_request, events.NewRequest)
    config.add_subscriber(on_new_response, events.NewResponse)
    return config.make_wsgi_app()
