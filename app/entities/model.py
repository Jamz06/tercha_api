from pydantic import BaseModel

# http ansewrs Заглушка, пока с ответами не определился
class DogDTO(BaseModel):
    id: int
    name: str
    owner: int
    model_config = {
        "json_schema_extra": {
            "example": {
                
                "id": 12423123,
                "name": "Бобик",
                "owner": 1
            }
        }
    }