from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy import text

from app.core.decorators.generals import close_session


# First view, available at http://localhost:6543/
@view_config(route_name='home')
@close_session
def home(request):
    sql = text('select * from tempresa')
    result = request.dbsession.execute(sql)
    for r in result:
        print(r)
    return Response('<body>Visit <a href="/howdy">hello</a></body>')


# /howdy
@view_config(route_name='hello')
@close_session
def hello(request):
    return Response('<body>Go back <a href="/">home</a></body>')
