from django.contrib import admin
from .models import Article, ArticleReview
# Register your models here.

admin.site.register(Article)
admin.site.register(ArticleReview)