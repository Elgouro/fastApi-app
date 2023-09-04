from fastapi import FastAPI
from fastapi import APIRouter
from app.routes.todo import todo_router
from app.models.model import Todo


router = APIRouter()
app = FastAPI()

@app.get("/")
def roots():
    return f'je suis dans le bon vieu temps'

app.include_router(todo_router)