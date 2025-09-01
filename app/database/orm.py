# from app.config import config
from sqlalchemy.orm import selectinload
from sqlalchemy import insert, select
from database.database import engine, Base, session_factory
from entities.db_model import Dog, Owner, Card, CardType, Sport, TaskStatus, Task

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
            # Владелец + собаки
            # owner = Owner(username='Kassandra', t_chat_id='122334')
            owners = [
                {"username": "Kassandra", "t_chat_id": 1223314},
                {"username": "Asya", "t_chat_id": 122332}
            ]
            # dog1 = Dog(name='Terra', owner_id=1)
            dogs = [
                {"name": "Терра", "owner_id": 1},
                {"name": "Мышь", "owner_id": 1},
                {"name": "Чиза", "owner_id": 1},
                {"name": "Эска", "owner_id": 1},
                {"name": "Гречка", "owner_id": 1},
                {"name": "Макс", "owner_id": 2},
                {"name": "Рульф", "owner_id": 2}
            ]
            sport = [
                {"name": "Тестовый спорт"}
            ]

            card_types = [
                {"name": "Зеленая", "dificulty": 1, "sport": 1},
                {"name": "Желтая", "dificulty": 2, "sport": 1},
                {"name": "Красная", "dificulty": 3, "sport": 1}
            ]

            cards = [
                {"name": "Тестовая 1 Зеленая", "description": "Тест1", "points": 1, "card_type_id": 1},
                {"name": "Тестовая 2 Желтая", "description": "Тест2 посложнее", "points": 10, "card_type_id": 2},
                {"name": "Тестовая 3 Красная", "description": "Тест3 самая сложная", "points": 100, "card_type_id": 3},
                {"name": "Тестовая 4 Зеленая", "description": "Тест4 легко, но много баллов", "points": 50, "card_type_id": 1},
            ]
            statuses = [
                {"name": "Открыта", "task_closed": False},
                {"name": "Закрыта", "task_closed": True},
            ]
            tasks = [
                {"dog": 1, "card": 1, "status": 1},
                {"dog": 1, "card": 2, "status": 1},
                {"dog": 2, "card": 1, "status": 1},
                {"dog": 3, "card": 1, "status": 1},
                {"dog": 3, "card": 1, "status": 1},
            ]

            session.execute(insert(Owner).values(owners))
            session.execute(insert(Dog).values(dogs))
            session.execute(insert(Sport).values(sport))
            session.execute(insert(CardType).values(card_types))
            session.execute(insert(Card).values(cards))
            session.execute(insert(TaskStatus).values(statuses))
            session.execute(insert(Task).values(tasks))

            
            session.commit()

    @staticmethod
    def get_owners_with_dogs():
        '''
            Получить владельцев с собаками
        '''

        with session_factory() as session:
            query = select(Owner).filter(Owner.id == 1).options(selectinload(Owner.dogs))
            # Посмотреть какой запрос составился
            print(query.compile())

            res = session.execute(query)

            result = res.scalars().first()
            return result
            
