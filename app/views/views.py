from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy import text

from app.core.decorators.generals import close_session
from app.models.shared.auth import Auth


# First view, available at http://localhost:6543/
@view_config(route_name='home')
@close_session
def home(request):
    test = request.dbsession.query(Auth).filter_by(id=1)
    print(test.scalar())
    # spongebob = User(
    #     name="bob",
    #     last_name="sponge",
    #     fullname="Spongebob Squarepants",
    #     username="spongeuser",
    #     addresses=[Address(email_address="spongebob@sqlalchemy.org")],
    # )

    # request.dbsession.add_all([spongebob])
    # request.dbsession.commit()
    return Response('<body>Visit <a href="/howdy">hello</a></body>')


# /howdy
@view_config(route_name='hello')
@close_session
def hello(request):
    return Response('<body>Go back <a href="/">home</a></body>')
