from fastapi import APIRouter, HTTPException, status,Depends
from models.events import Events, events_pydantic_list, events_pydantic
from tortoise.contrib.fastapi import  HTTPNotFoundError
from routers.users import User

event_router = APIRouter(tags=["Event"],)


@event_router.get('/')
async def users_all():
    return await events_pydantic_list.from_queryset(Events.all())


# @event_router.post("/add",response_model=events_pydantic_list)
# async def add_user(event:events_pydantic, user:User=Depends()):
#     new_event = await Events.create(**event.dict(exclude_unset=True))
#     return await events_pydantic_list.from_tortoise_orm(new_event)