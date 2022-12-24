from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Article, ArticleReview
from django.views import View
from .forms import ArticleForm, ArticleReviewForm
from main.models import Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404
# Create your views here.

class ArticleDetailView(View):
    def get(sellf, request, slug, id):
        article = get_object_or_404(Article, id=id, slug=slug)
        
        context = {
            "article":article,
            'form': ArticleReviewForm(data=request.POST)
        }
        return render(request, 'articles/detail.html', context)
    
    def post(self, request, slug, id):
        article = get_object_or_404(Article, id=id, slug=slug)
        review_form = ArticleReviewForm(data=request.POST)

        if review_form.is_valid():
          
          
            ArticleReview.objects.create(
                article=article,
                user=request.user,
                stars_given=review_form.cleaned_data['stars_given'],
                body=review_form.cleaned_data['body']
            )

            return redirect(reverse("article-detail", kwargs={"id": article.id, 'slug':article.slug}))
        else: 
            return render(request, 'articles/detail.html', {'form': review_form, 'article':article})
    
class UpdateArticleView(View, LoginRequiredMixin):
    def get(self, request, slug, id):
        
        article = get_object_or_404(Article, id=id, slug=slug)
        if request.user == article.author:
            article_form = ArticleForm(instance=article)
            return render(request, "articles/edit_article.html", {"article": article, "form": article_form})    
        else:
            messages.error(request, "You do not have a permission!")
            return redirect('index')
        
    def post(self, request, slug, id):
        article = get_object_or_404(Article, id=id, slug=slug)
        article_form = ArticleForm(instance=article, data=request.POST)

        if article_form.is_valid():
            article_form.save()
            messages.success(request, "Successfully changed.")
            return redirect(reverse("article-detail", kwargs={"id": id, 'slug':slug}))

        return render(request, "books/edit_article.html", {"article": article, "form": article_form})
    
class CreateArticleView(View, LoginRequiredMixin):
    def get(self, request):
        article_form = ArticleForm()
        context = {
            "form": article_form
        }
        return render(request, "articles/new_article.html", context)

    def post(self, request):
        article_form = ArticleForm(data=request.POST)

        if article_form.is_valid():
            data = article_form.cleaned_data
            article = Article.objects.create(
                title=data['title'],
                body = data['body'],
                author = request.user
            )
            for i in data['categories']:
                article.categories.add(i)
            article.save()
            messages.success(request, "Succesfully created.")
            return redirect(reverse("article-detail", kwargs={"id": article.id, "slug":article.slug}))
        else:
            context = {
                "form": article_form
            }
            messages.error(request, "Something went wrong!")
            return render(request, "articles/new_article.html", context)

class DeleteArticleView(View, LoginRequiredMixin):
    def get(self, request, id):
        article = Article.objects.filter(id=id, author=request.user).first()
        if article:
            article.delete()
            messages.success(request, "Article is successfully deleted.")
            return redirect('index')
        else:
            messages.error(request, "You do not have a permission!")
            return redirect("index")

class UpdateArticleReview(View, LoginRequiredMixin):
    def get(self, request, id):
        review  =  get_object_or_404(ArticleReview, id=id)
        if request.user == review.user:
            review_form = ArticleReviewForm(instance=review)
            return render(request, 'articles/edit_articlereview.html', {'form':review_form})
        else:
            messages.warning(request, "You do not have a permission!")
            return redirect(reverse("article-detail", kwargs={"id": review.article.id, 'slug':review.article.slug}))
        
    def post(self, request, id):
        review  =  get_object_or_404(ArticleReview, id=id) 
        review_form = ArticleReviewForm(instance=review, data=request.POST)   
        if review_form.is_valid():
            review_form.save()
            messages.success(request, "Successfully changed.")
            return redirect(reverse("article-detail", kwargs={"id": review.article.id, 'slug':review.article.slug}))
        else:
            messages.warning(request, "Something went wrong!")
            return render(request, 'articles/edit_articlereview.html', {'form':review_form})
       
class DeleteArticleReView(View, LoginRequiredMixin):
    def get(self, request, id):
        review = ArticleReview.objects.filter(id=id, user=request.user).first()
        if review:
            review.delete()
            messages.success(request, "Article is successfully deleted.")
            return redirect('index')
        else:
            messages.error(request, "You do not have a permission!")
            return redirect("index")        