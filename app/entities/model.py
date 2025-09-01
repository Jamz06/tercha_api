from pydantic import BaseModel

# http ansewrs Заглушка, пока с ответами не определился
class DogDTO(BaseModel):
    id: int
    name: str
    owner_id: int
    model_config = {
        "json_schema_extra": {
            "example": {                
                "id": 12423123,
                "name": "Бобик",
                "owner": 1
            }
        }
    }

class OwnerDTO(BaseModel):
    id: int
    username: str
    t_chat_id: int

class OwnerDogsDTO(OwnerDTO):
    dogs: list["DogDTO"]


class CardDTO(BaseModel):
    id: int
    name: str
    description: str
    points: int
    card_type_id: int


class TaskStatusDTO(BaseModel):
    id: int
    name: str
    task_closed: bool


class TaskDTO(BaseModel):
    id: int
    dog: str
    card: str
    status: str
   

class TasksDTO(BaseModel):
    owner_id: int
    tasks: list[TaskDTO]