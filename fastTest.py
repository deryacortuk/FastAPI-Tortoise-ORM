from fastapi import FastAPI,HTTPException
from modelsTortoise import users_pydandic_list,user_pydantic,UserModel

from tortoise.contrib.fastapi import register_tortoise, HTTPNotFoundError
from pydantic import BaseModel

class Message(BaseModel):
    message :str

app = FastAPI()

@app.get('/')
async def index():
    return {"fastapi":"tortoise"}

@app.post('/user',response_model=users_pydandic_list)
async def add_user(user: user_pydantic):
    objt = await UserModel.create(**user.dict(exclude_unset =True))
    return await users_pydandic_list.from_tortoise_orm(objt)


@app.get('/user/{id}',response_model=users_pydandic_list,responses = {404:{"model":HTTPNotFoundError}})
async def seach_user(id:int):
    return await users_pydandic_list.from_queryset_single(UserModel.get(id=id))

@app.put('/user/{id}',response_model=users_pydandic_list,responses={404:{"model":HTTPNotFoundError}})
async def user_update(id :int, user:user_pydantic):
    await UserModel.filter(id=id).update(**user.dict(exclude_unset = True))
    return await users_pydandic_list.from_queryset_single(UserModel.get(id=id))

@app.delete('/user/{id}',response_model=Message,responses={404:{"model":HTTPNotFoundError}})
async def user_delete(id:int):
    obj = await UserModel.filter(id=id).delete()
    if not obj:
        raise HTTPException(status_code=404,detail="User is not found!!!")
    return Message(message ="User is deleted successfully")

@app.get('/user')
async def users_all():
    return await users_pydandic_list.from_queryset(UserModel.all())


register_tortoise(
    app,
    db_url = "sqlite://store.db",
    modules ={'models':['modelsTortoise']},
    generate_schemas = True,
    add_exception_handlers = True,
)