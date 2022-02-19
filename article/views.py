from typing import List

from django.shortcuts import render
from ninja import NinjaAPI, ModelSchema

from .models import Article

# Create your views here.
api = NinjaAPI()


class ArticleSchema(ModelSchema):
    class Config:
        model = Article
        # model_fields = ('id', 'title', 'content', 'created_at')
        model_fields = '__all__'


@api.get('')
def get_articles(request):
    articles = Article.objects.all()
    return [
        {
            'id': article.id,
            'title': article.title,
            'content': article.content,
            'created_at': article.created_at,
        }
        for article in articles
    ]


@api.post('')
def create_article(request, payload: ArticleSchema):
    article = Article.objects.create(**payload.dict())
    return {'id': article.id}
