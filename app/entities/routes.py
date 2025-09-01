from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from entities import model 

from entities import db_model 
from entities import queries

from config import config


entities_router = APIRouter()

@entities_router.get(
    '/dog/{dog_id}', tags=['dog'],
    summary="Получить данные по собаке по ид",
    status_code=200,
    response_model=model.DogDTO,
)
async def get_dog(dog_id: int)->model.DogDTO:
    """
        Получить данные по собаке по ID
    """
    
    result = queries.get_dog_by_id(dog_id)
    

    return result


@entities_router.get(
    '/owner/{chat_id}', tags=['owner'],
    summary="Получить данные по владельцу по chat_id",
    status_code=200,
    response_model=model.OwnerDogsDTO,
)
async def get_dog(chat_id: int)->model.OwnerDogsDTO:
    """
        Получить данные юзера по ид чата в телеге
    """
    
    result = queries.get_owner_with_dogs(chat_id)
    # Можно не конвертить в модель ответа, если они похожи и в response_model стоит нужная
    # pydantic ее сам валидирует

    return result

@entities_router.get(
    '/tasks/{owner_id}', tags=['tasks'],
    summary="Получить все задачи пользователя, с собаками",
    status_code=200,
    response_model=model.TasksDTO
)
async def get_owner_tasks(owner_id: int):
    """
        Получить все задачи пользователя по owner_id
    """

    result = queries.get_owner_tasks(owner_id)
    response = model.TasksDTO(
        owner_id=owner_id,
        tasks=result
    )
    return response