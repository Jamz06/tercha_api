# from app.config import config

from database.database import engine, Base, session_factory
from entities.db_model import Dog, Owner

class Orm:
    '''
        объект для управления БД
    '''
    @staticmethod
    def init_db():
        '''
            Создать пустые таблицы из описанных моделью классов
        '''
        engine.echo = True
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    @staticmethod
    def insert_test_data():
        '''
            Создать тестовые данные
        '''

        with session_factory() as session:
            owner = Owner(username='Kassandra', t_chat_id='122334')
            session.add(owner)
            session.flush()
            dog = Dog(name='Terra', owner=owner.id)
            session.add(dog)
            session.commit()
