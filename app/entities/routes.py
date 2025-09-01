from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from entities.model import DogDTO, OwnerDTO

from entities import db_model 
from entities import queries

from config import config


entities_router = APIRouter()

@entities_router.get(
    'dog/{dog_id}', tags=['dog'],
    summary="Получить данные по собаке по ид",
    status_code=200,
    response_model=DogDTO,
)
async def get_dog(dog_id: int)->DogDTO:
    """
        Получить данные по собаке по ID
    """
    
    result = queries.get_dog_by_id(dog_id)
    

    return result


@entities_router.get(
    'owner/{chat_id}', tags=['owner'],
    summary="Получить данные по владельцу по chat_id",
    status_code=200,
    response_model=OwnerDTO,
)
async def get_dog(chat_id: int)->OwnerDTO:
    """
        Получить данные юзера по ид чата в телеге
    """
    
    result = queries.get_owner_with_dogs(chat_id)
    

    return result
