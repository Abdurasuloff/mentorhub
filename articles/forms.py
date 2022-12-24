from .models import Article, ArticleReview
from django.forms import ModelForm
from django import forms


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'body', 'categories')
        
class ArticleReviewForm(ModelForm):
    stars_given = forms.IntegerField(min_value=1, max_value=5)
    body = forms.CharField(max_length=100)
    class Meta:
        model = ArticleReview
        fields = ('body', 'stars_given')        