from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from entities.model import DogDTO

from entities import db_model 
from entities import queries

from config import config


entities_router = APIRouter()

@entities_router.get(
    'dog/{dog_id}', tags=['dogs'],
    summary="Получить данные по собаке по ид",
    status_code=200,
    response_model=DogDTO,
)
async def get_dog(dog_id: int)->DogDTO:
    """
        Получить данные по собаке по ID
    """
    # Заглушка
    result = queries.get_dog_by_id(dog_id)
    

    return result
