from pyramid.config import Configurator

from sqlalchemy import engine_from_config, create_engine
from sqlalchemy.orm import configure_mappers, sessionmaker
from sqlalchemy.pool import NullPool

import zope.sqlalchemy

# run configure_mappers after defining all of the models to ensure
# all relationships can be setup
configure_mappers()

def get_engine(settings, prefix='initdb.'):
    return engine_from_config(settings, prefix)


def get_session_factory(engine):
    factory = sessionmaker()
    factory.configure(bind=engine)
    return factory


def get_tm_session(session_factory, transaction_manager):
    """
    Get a ``sqlalchemy.orm.Session`` instance backed by a transaction.

    This function will hook the session to the transaction manager which
    will take care of committing any changes.

    - When using pyramid_tm it will automatically be committed or aborted
      depending on whether an exception is raised.

    - When using scripts you should wrap the session in a manager yourself.
      For example::

          import transaction

          engine = get_engine(settings)
          session_factory = get_session_factory(engine)
          with transaction.manager:
              dbsession = get_tm_session(session_factory, transaction.manager)

    """
    dbsession = session_factory()
    zope.sqlalchemy.register(
        dbsession, transaction_manager=transaction_manager)
    return dbsession

def crea_session(url=None, schemas=None):

    settings = {'pyramid.includes': 'pyramid_debugtoolbar pyramid_tm'}
    settings['tm.manager_hook'] = 'pyramid_tm.explicit_manager'

    config = Configurator(settings=settings)
    config.include('pyramid_tm')
    config.include('pyramid_retry')

    engine = create_engine(url, poolclass=NullPool)
    autocommit_engine = engine.execution_options(isolation_level="AUTOCOMMIT")
    session_factory = get_session_factory(autocommit_engine)
    config.registry['dbsession_factory'] = session_factory
    config.add_request_method(
        # r.tm is the transaction manager used by pyramid_tm
        lambda r: get_tm_session(session_factory, r.tm),
        'dbsession',
        reify=True
    )

    session = session_factory()

    if schemas is not None:  # Valida si hay cambios en nombre de esquemas
        session.connection(
            execution_options={
                "schema_translate_map": schemas
            })

    return session



def includeme(config):
    """
    Initialize the model for a Pyramid app.
    Activate this setup using ``config.include('app.models')``.
    """
    pass
