from .models import Course, Chapter, Lesson
from django import forms
from ckeditor_uploader.fields import RichTextUploadingFormField

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title", 'subtitle', "description", "cover_photo", "is_active", 'categories')
        

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ('title', "is_active")
    
class LessonForm(forms.ModelForm):
    body = RichTextUploadingFormField()
    class Meta:
        model = Lesson 
        fields = ("title", 'body', "is_active")        