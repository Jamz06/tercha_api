from sqlalchemy import select

from database.database import get_db, session_factory
# from database.models import dogs_table
from entities.db_model import Dog
from entities import model

def get_dog_by_id(id: int):
    with session_factory() as session:
        dog = session.query(Dog).filter(Dog.id  == id).first()
        dog = model.DogDTO.model_validate(dog, from_attributes=True)
    return dog

