from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Optional,List

from pydantic.env_settings import SettingsSourceCallable

app =FastAPI(title="ToDo API")

class ToDo(BaseModel):
    name:str
    date_due:str
    description:str

store_Tolist =[]

app.get("/")
async def index():
    return {"FastApi":"pydantic"}

@app.post('/list/')
async def create_list(todo:ToDo):
    store_Tolist.append(todo)
    return todo
@app.get('/todo/',response_model=List[ToDo])
async def get_todo_list():
    return store_Tolist

@app.get('list/{id}')
async def  get_todo(id:int):
    try:
        return store_Tolist[id]
    except:
        raise HTTPException(status_code=404,detail="todo not found")

@app.put('/list/{id}')
async def update_todo(id:int,todo:ToDo):
    try:
        store_Tolist[id]=todo
        return store_Tolist
    except:
        raise HTTPException(status_code=404,detail="todo not found")

@app.delete('/todo/{id}')
async def delete_todo(id:int,todo:ToDo):
    try:
        delete_obj = store_Tolist[id]
        store_Tolist.pop(id)
        return delete_obj
    except:
        raise HTTPException(status_code=404,detail="todo not found")

    
    









