from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError

def configure_sqlalchemy(settings):
    url = settings.get('sqlalchemy.url')

    try:
      engine = create_engine(
        url,
        pool_pre_ping=True,
        pool_size=int(settings.get('sqlalchemy.pool_size')),
        max_overflow=int(settings.get('sqlalchemy.max_overflow')),
        pool_timeout=int(settings.get('sqlalchemy.pool_timeout'))
      )
      engine.connect().execution_options(autocommit=True)
      print('Conexión exitosa')
    except SQLAlchemyError as e:
      print('Error al conectar a la base de datos:', str(e))

    session_factory = sessionmaker(bind=engine)
    session = scoped_session(session_factory)
    return session

def create_session(event):
  try:
    dbsession_factory = event.request.registry['dbsession_factory']
    dbsession = dbsession_factory()
    print('Session creada')
    return dbsession
  except SQLAlchemyError as e:
    print('Error al crear session:', str(e))
