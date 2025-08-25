from fastapi import FastAPI, APIRouter

from config import config

from entities.routes import entities_router

app = FastAPI()
main_router = APIRouter()

main_router.include_router(entities_router, prefix='/entities', tags=['entities'])


app.include_router(main_router)