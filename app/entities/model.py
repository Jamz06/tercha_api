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
    dogs: list["DogDTO"]
