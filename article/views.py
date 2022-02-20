from typing import List
from django.shortcuts import get_object_or_404

from ninja import NinjaAPI

from .models import Article
from .schemas import ArticleSchema


api = NinjaAPI()


@api.get('', response=List[ArticleSchema])
def get_articles(request):
    articles = Article.objects.all().order_by('-pk')
    return articles


@api.get('/{article_id}/', response=ArticleSchema)
def get_article(request, article_id: int):
    article = get_object_or_404(Article, id=article_id)
    return article


@api.post('')
def create_article(request, payload: ArticleSchema):
    article = Article.objects.create(**payload.dict())
    return {
        'id': article.id,
        'title': article.title,
        'content': article.content,
        'created_ad': article.created_at
    }
