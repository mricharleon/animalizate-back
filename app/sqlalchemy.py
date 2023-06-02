from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError

def configure_sqlalchemy(settings):
    url = settings.get('sqlalchemy.url')

    try:
      engine = create_engine(url, pool_pre_ping=True)
      engine.connect().execution_options(autocommit=True)
      print('Conexión exitosa')
    except SQLAlchemyError as e:
      print('Error al conectar a la base de datos:', str(e))

    session_factory = sessionmaker(bind=engine)
    session = scoped_session(session_factory)
    return session

def create_session(Session):
  try:
    session = Session()
    print('Session creada')
    return session
  except SQLAlchemyError as e:
    print('Error al crear session:', str(e))
