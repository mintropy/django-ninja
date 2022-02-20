# from typing import 

from ninja import ModelSchema

from .models import Article


class ArticleSchema(ModelSchema):
    # id: int
    # title : str
    # content: str
    # created_at: str
    
    class Config:
        model = Article
        model_fields = '__all__'
