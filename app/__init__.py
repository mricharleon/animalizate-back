from pyramid import events
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response('<body><h1>Hello World!</h1></body>')


def on_new_request(event):
    # schema_name = _figire_out_schema_name_from_request(event.request)
    schema_name = 'public'
    DBSession.execute("SET search_path TO %s" % schema_name)

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    config = Configurator(settings=settings)
    config.include('.routes.global')
    config.include('.models')
    config.scan('.views.views')

    config.add_subscriber(on_new_request, events.NewRequest)
    return config.make_wsgi_app()
