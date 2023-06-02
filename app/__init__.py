from pyramid import events
from pyramid.config import Configurator
from pyramid.response import Response
from .sqlalchemy import configure_sqlalchemy, create_session, text

test=None


def hello_world(request):
    return Response('<body><h1>Hello World!</h1></body>')


def on_new_request(event):
    # schema_name = _figire_out_schema_name_from_request(event.request)
    session = create_session(test)
    schema_name = 'init'
    session.execute(text("SET search_path TO %s" % schema_name))
    sql = text('select * from tempresa')
    result = session.execute(sql)
    for r in result:
        print(r)
    # session.close()
    # session.get_bind().dispose()

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
