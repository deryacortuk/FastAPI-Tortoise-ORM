from tortoise import fields, models 
from tortoise.contrib.pydantic import pydantic_model_creator

class UserModel(models.Model):

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    username = fields.CharField(max_length=50)
    is_active = fields.BooleanField(default=True)
    created_date = fields.DatetimeField(auto_now_add=True)
    modified_date = fields.DatetimeField(auto_now=True)

    
    class Meta:
        ordering = ["name"]

    class PydanticMeta:
        exclude = ("created_date",)

users_pydandic_list= pydantic_model_creator(UserModel,name="User Model")
user_pydantic =pydantic_model_creator(UserModel,name="User",exclude_readonly=True)
