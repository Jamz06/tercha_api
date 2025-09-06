from sqlalchemy import select, and_
from sqlalchemy.orm import selectinload, aliased

from database.database import get_db, session_factory
# from database.models import dogs_table
from entities.db_model import Card, Dog, Owner, Sport, Task, TaskStatus
from entities.model_utils import DbAnswers
from entities import model

# ----------------------------------- OWNER ---------------------------------- #
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

def insert_owner(chat_id: int, username:str)->DbAnswers:
    '''
    Создать владельца собаки
    '''
    result = DbAnswers.ERROR
    
    try:
        with session_factory() as session:
            exists = session.query(Owner).where(Owner.t_chat_id == chat_id).first()
            if not exists:
                owner = Owner(t_chat_id=chat_id, username=username)
                session.add(owner)
                session.commit()
                result = DbAnswers.SUCCESS
            else:
                result = DbAnswers.DUP_VAL

    except Exception as err:
        result = DbAnswers.ERROR
        # Записать ошибку в лог

    return result
          

# ------------------------------------ DOG ----------------------------------- #
def get_dog_by_id(id: int):
    with session_factory() as session:
        dog = session.query(Dog).filter(Dog.id  == id).first()
        dog = model.DogDTO.model_validate(dog, from_attributes=True)
    return dog

def insert_dog(name: str, owner: int):
    result = DbAnswers.ERROR
    
    try:
        with session_factory() as session:
            exists = (
                session.query(Dog).where(and_(
                        Dog.name == name,
                        Dog.owner_id == owner
                    )
                )
            .first()
            )
            if not exists:
                dog = Dog(name=name, owner_id=owner)
                session.add(dog)
                session.commit()
                result = DbAnswers.SUCCESS
            else:
                result = DbAnswers.DUP_VAL

    except Exception as err:
        result = DbAnswers.ERROR
        # Записать ошибку в лог

    return result
# ----------------------------------- TASK ----------------------------------- #


        
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

def get_owner_tasks(owner_id: int):
    '''
        Получить все задачи пользователя по owner_id
    '''

    t = aliased(Task)
    c = aliased(Card)
    d = aliased(Dog)
    s = aliased(TaskStatus)

    # В следующий раз проще обычный запрос написать :)
    query = (
        select(
            t.id,
            d.name,
            c.name,
            s.name
        )
        .outerjoin(c, c.id == t.card)   # LEFT JOIN card c ON c.id = t.card
        .join(d, t.dog == d.id)          # INNER JOIN dog d ON t.dog = d.id
        .join(s, s.id == t.status)       # INNER JOIN task_status s ON s.id = t.status
        .filter(
            d.owner_id == owner_id,      # :owner_id parameter
            s.task_closed == False       # s.task_closed = 'False'
        )
    )

    with session_factory() as session:
        res = session.execute(query)
        result = res.all()
        
        # Времени мало, потом мб че поизящнее придумаю
        # Развернуть в список моделей задач, для ответа
        tasks = [model.TaskDTO(id=row[0], dog=row[1], card=row[2], status=row[3]) for row in result]
    return tasks




def get_dog_tasks(dog_id: int, status_id: int):
     '''
        Получить задачи по собаке, со статусом
     '''
     pass

