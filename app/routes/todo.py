from fastapi import APIRouter, Path
from app.models.model import Todo, TodoItem
from typing import List

todo_router = APIRouter()




todo_list = []
# nous avons une liste de todo qui nous sert a stocker nos todo
#comme notre fonction prend en entre une liste de todo alors en faisant 
#todo_list.append() on cree une liste de liste pas tres interessant
#todo_list.extend() permet plutot d'avoir une liste d'objet cool
@todo_router.post('/todo')
async def add_todo(todo: List[Todo])-> dict:
    todo_list.extend(todo)
    #return {'message': 'todo added succesfully'}
    #return f"message:{len(todos)} was added successfully"
    return {'message': f'{len(todo)} todos added successfully'}

@todo_router.get('/todo')
async def retrieve_todo()-> dict:
    return {"all todos are ": todo_list}

@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int= Path(..., title = "The ID of the todo we have to retrieve")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return{
                "todo":todo
            }
    return{
        "message":"Todo with this ID doesn't exist in our database"
    }
    

@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title= "the id of todo to update"))-> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return{
                "message": "Todo updated successfully"
            }
    return {
        "message": "todo with this id was not found to be update"
    }
@todo_router.delete("/todo")
async def delete_all_todo()-> dict:
    todo_list.clear()
    return {
        "message":"All todos has been deleted successfully"
    }

@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int = Path(...,title="this is for deleting our preview todo post")) ->dict:
    for todo in todo_list :
        if todo.id == todo_id:
            todo_list.pop(todo)
            return {"message":"Todo has been deleted successfully"}
    return {
        "message":"we can't delete the doto your are asking for cause id was not found"
    }