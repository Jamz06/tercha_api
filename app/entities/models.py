from pydantic import BaseModel

# http ansewrs Заглушка, пока с ответами не определился
class Result(BaseModel):
    id: int
    name: str
    user: int
    model_config = {
        "json_schema_extra": {
            "example": {
                
                "id": 12423123,
                "name": "Бобик",
                "user": 1
            }
        }
    }