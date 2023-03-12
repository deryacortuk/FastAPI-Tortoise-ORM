from tortoise import fields, models  ,Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel

class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20)
    email = fields.CharField(100, unique=True, index=True)
    is_active = fields.BooleanField(default=False, null=False)
    created_at = fields.DatetimeField(auto_now_add=True, null=True)
    updated_at = fields.DatetimeField(auto_now=True,null=True)
    
    
    class Meta:
        ordering = ("username",)
        
    class PydanticMeta:
        exclude = ("created_at",)
        
class Message(BaseModel):
    message:str


users_pydantic_list = pydantic_model_creator(User, name="User")
user_pydantic = pydantic_model_creator(User, name="User", exclude_readonly=True)