from .views import ArticleDetailView, UpdateArticleView, CreateArticleView, DeleteArticleView, UpdateArticleReview, DeleteArticleReView
from django.urls import path 

app_name = "article"
urlpatterns = [
    path('<int:id>/<slug:slug>/detail', ArticleDetailView.as_view(), name='detail'),
    path('<int:id>/<slug:slug>/update', UpdateArticleView.as_view(), name='update'),
    path('<int:id>/delete', DeleteArticleView.as_view(), name="delete" ),
    path('new', CreateArticleView.as_view(), name ='new' ),
    
    path('review/<int:id>/update', UpdateArticleReview.as_view(), name="review-update"),
    path('review/<int:id>/delete', DeleteArticleReView.as_view(), name="review-delete"),
    
]