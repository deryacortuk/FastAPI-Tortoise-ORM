from fastapi import FastAPI
import uvicorn
from routers.users import user_router
from routers.events import event_router
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()


register_tortoise(
    app,
  db_url="sqlite://db.sqlite3",
    modules={"models": ["models.users","models.events"]},
    generate_schemas=True,
    add_exception_handlers=True,
  
)

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")


@app.get("/")
async def index():
    return {"Do something!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1",port= 8080, reload=True)