from tortoise import fields, models 
from tortoise.contrib.pydantic import pydantic_model_creator



class Events(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=20)
    content = fields.TextField()
    user = fields.ForeignKeyField("models.User", related_name="users")
    created_at = fields.DatetimeField(auto_now_add=True, null=True)
    updated_at = fields.DatetimeField(auto_now=True,null=True)
    
    
    class Meta:
        ordering = ("-created_at",)
        
    class PydanticMeta:
        exclude = ("created_at",)

events_pydantic_list = pydantic_model_creator(Events, name="Events")
events_pydantic = pydantic_model_creator(Events, name="Events", exclude_readonly=True)