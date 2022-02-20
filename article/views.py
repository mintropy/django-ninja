from typing import List
from django.shortcuts import get_object_or_404

from ninja import NinjaAPI
from ninja_extra import (
    NinjaExtraAPI, api_controller,
    http_get, http_post
)

from .models import Article
from .schemas import ArticleSchema


api = NinjaExtraAPI()


@api_controller
class ArticleAPI:

    @http_get('', response=List[ArticleSchema])
    def get_articles(self):
        articles = Article.objects.all().order_by('-pk')
        return articles

    @http_get('/{article_id}/', response=ArticleSchema)
    def get_article(self, article_id: int):
        article = get_object_or_404(Article, id=article_id)
        return article

    @http_post('')
    def create_article(self, payload: ArticleSchema):
        article = Article.objects.create(**payload.dict())
        return {
            'id': article.id,
            'title': article.title,
            'content': article.content,
            'created_ad': article.created_at
        }


api.register_controllers(ArticleAPI)
