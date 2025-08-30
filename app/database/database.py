from sqlalchemy import create_engine

from sqlalchemy.orm import DeclarativeBase, sessionmaker


from config import config


def dsn_make():
    db = config['db']
    return f"{db['driver']}://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}"

engine = create_engine(
    url = dsn_make(),
    echo=config['main']['debug']
)


session_factory = sessionmaker(engine)

def get_db():
    db = session_factory()
    try:
        yield db
    finally:
        db.close()

class Base(DeclarativeBase):
    pass