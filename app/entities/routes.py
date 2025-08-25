from fastapi import APIRouter

from config import config


entities_router = APIRouter()

@entities_router.get(
    'dog/{dog_id}', tags=['dogs'],
    summary="Получить данные по собаке по ид",
    status_code=200,
    response_model=ResultDog,
)
async def get_dog(dog_id: int)->Result:
    """
        Получить данные по собаке по ID
    """
    # Заглушка
    result = Result()
    pass

    return result
