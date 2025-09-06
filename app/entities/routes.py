from fastapi import APIRouter, Depends, HTTPException, Query

from typing import Annotated



from entities import model 

from entities import db_model 
from entities import queries

from config import config
from entities.model_utils import DbAnswers


entities_router = APIRouter()
# ----------------------------------- OWNER ---------------------------------- #
# GET OWNER
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

# INSERT OWNER
@entities_router.post(
    '/owner', tags=['owner'],
    summary="Создать владельца",
    status_code=201,
        responses={
             409: {'detail': 'Duplicate entry'}
    },
    response_model=model.BaseResponse,
)
async def create_owner(
    chat_id: int,
    first_name: str,
    second_name: str,

)->model.BaseResponse:
    """
        Создать юзера
    """
    response = model.BaseResponse(success=False)

    result = queries.insert_owner(chat_id=chat_id, username=first_name)  
    
    
    if result == DbAnswers.DUP_VAL:
        raise HTTPException(status_code=409,detail='Duplicate entry')
    
    if result == DbAnswers.SUCCESS:
        response.success = True
    
    if result == DbAnswers.ERROR:
        response.success == False

    return response


# ------------------------------------ DOG ----------------------------------- #
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

# INSERT DOG
@entities_router.post(
    '/dog', tags=['dog'],
    summary="Создать собаку",
    status_code=201,
        responses={
             409: {'detail': 'Duplicate entry'}
    },
    response_model=model.BaseResponse,
)
async def create_dog(
    
    name: str,
    owner: str,

)->model.BaseResponse:
    """
        Создать собаку
    """
    response = model.BaseResponse(success=False)

    result = queries.insert_dog(name, owner)
    

    if result == DbAnswers.DUP_VAL:
        raise HTTPException(status_code=409,detail='Duplicate entry')
    
    if result == DbAnswers.SUCCESS:
        response.success = True
    
    if result == DbAnswers.ERROR:
        response.success == False

    return response




# ----------------------------------- TASK ----------------------------------- #
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


