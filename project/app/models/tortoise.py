# from pydantic import ConfigDict
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model


class TextSummary(Model):
    # model_config = ConfigDict(from_attributes=True)

    url = fields.TextField()
    summary = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.url

    # class Config:
    #     orm_mode=True


print("About to create SummarySchema")
SummarySchema = pydantic_model_creator(TextSummary)
