from django.db import models
from users.models import CustomUser
from slugify import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from main.models import Category
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    body = RichTextUploadingField()
    time = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def get_overall_stars(self):
        reviews = ArticleReview.objects.filter(article_id = self.id)
        count = reviews.count()
        all_stars = 0
        for i in reviews:
            all_stars += i.stars_given
            
        return all_stars/count


class ArticleReview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    article  = models.ForeignKey(Article, on_delete=models.CASCADE)
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    stars_given = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], default=1
    )
    
    def __str__(self):
        return str(self.user.username) + "is commented" + str(self.article.title)       
    
    
    
# some signals
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Article)
def save_profile(sender, instance, created, **kwargs):
    if created:
        title  = instance.title
        instance.slug = slugify(title, max_length=25 )
        instance.save()        
        
    