from sqlalchemy import select
from sqlalchemy.orm import selectinload

from database.database import get_db, session_factory
# from database.models import dogs_table
from entities.db_model import Dog, Owner, Sport, Task
from entities import model

def get_dog_by_id(id: int):
    with session_factory() as session:
        dog = session.query(Dog).filter(Dog.id  == id).first()
        dog = model.DogDTO.model_validate(dog, from_attributes=True)
    return dog

def get_owner_with_dogs(chat_id: int)->Owner:
        '''
            Получить владельцев с собаками
        '''

        with session_factory() as session:
            query =( 
                 select(Owner)
                .select_from(Owner) # Себе на будущее: это избыточно, но тебе нравится явно указывать таблицу sql-style 
                .where(Owner.t_chat_id == chat_id)
                .options(selectinload(Owner.dogs))
            )
            res = session.execute(query)
            # scalars - Для получения первых элементов кортежей, 
            # т.к. все равно придут кортежи с одним объектом
            result = res.scalars().first()
        return result
        
def get_sports():
    '''
        Получить виды спорта
    '''
    # ! Пока предпологается, что видов спорта до 5, поэтому нам не нужна фильтрация
    with session_factory() as session:
        query = select(Sport)
        res = session.execute(query)
        result = res.scalars().all()
    return result

def get_cards_by_sport(sport_id:int):
     '''
        Получить доступные карточки из вида спорта
     '''


def get_dog_tasks(dog_id: int, status_id: int)->Task:
     '''
        Получить задачи по собаке, со статусом
     '''
     pass

