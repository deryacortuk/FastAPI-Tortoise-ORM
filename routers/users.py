from fastapi import APIRouter, HTTPException, status
from models.users import user_pydantic, users_pydantic_list, User, Message
from tortoise.contrib.fastapi import  HTTPNotFoundError

user_router = APIRouter(tags=["User"],)

@user_router.post("/create",response_model=users_pydantic_list)
async def add_user(user:user_pydantic):
    new_user = await User.create(**user.dict(exclude_unset=True))
    return await users_pydantic_list.from_tortoise_orm(new_user)


@user_router.get("/{id}",response_model=users_pydantic_list,responses ={404:{"model":HTTPNotFoundError}})
async def get_user(id:int):
    return await users_pydantic_list.from_queryset_single(User.get(id=id))

@user_router.put("/update/{id}",response_model=users_pydantic_list,responses ={404:{"model":HTTPNotFoundError}})
async def update_user(id:int, user:user_pydantic):
    await User.filter(id=id).update(**user.dict(exclude_unset=True))
    return await users_pydantic_list.from_queryset(User.get(id=id))

@user_router.delete('/delete/{id}',response_model=Message,responses={404:{"model":HTTPNotFoundError}})
async def user_delete(id:int):
    obj = await User.filter(id=id).delete()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User was not found!!!")
    return Message(message ="User was deleted successfully")

@user_router.get('/')
async def users_all():
    return await users_pydantic_list.from_queryset(User.all())

