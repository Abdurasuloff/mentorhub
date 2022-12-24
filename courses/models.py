from django.db import models
from users.models import CustomUser
from main.models import Category
from ckeditor_uploader.fields import RichTextUploadingField
import uuid
# Create your models here.

class Course(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="course_author")
    attenders = models.ManyToManyField(CustomUser,  related_name="course_attenders", blank=True)
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField()
    cover_photo = models.ImageField(upload_to="cover_photos/", default='cover_photos/default_cover.png')
    time = models.DateTimeField(auto_now_add=True)
    slug = models.UUIDField(default=uuid.uuid4)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title 

class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="chapter_author")
    finished_students = models.ManyToManyField(CustomUser,  related_name="finished_students_of_chapter", blank=True)
    title = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    slug = models.UUIDField(default=uuid.uuid4)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title 
    
class Lesson(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="lesson_author")
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    finished_students = models.ManyToManyField(CustomUser, related_name="finished_students_of_lesson",  blank=True)
    title = models.CharField(max_length=250)
    body = RichTextUploadingField()
    time = models.DateTimeField(auto_now_add=True)
    slug = models.UUIDField(default=uuid.uuid4)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title 


# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from slugify import slugify

# @receiver(post_save, sender=Course)
# def slugify_course(sender, instance, created, **kwargs):
#     if created:
#         title  = instance.title
#         instance.slug = slugify(title, max_length=25 )
#         instance.save()        

# @receiver(post_save, sender=Chapter)
# def slugify_chapter(sender, instance, created, **kwargs):
#     if created:
#         title  = instance.title
#         instance.slug = slugify(title, max_length=25 )
#         instance.save()          

# @receiver(post_save, sender=Lesson)
# def slugify_course(sender, instance, created, **kwargs):
#     if created:
#         title  = instance.title
#         instance.slug = slugify(title, max_length=25 )
#         instance.save()      
    