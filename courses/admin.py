from django.contrib import admin
from .models import Course, Chapter, Lesson

class ChapterInline(admin.TabularInline):
    model = Chapter

class LessonInline(admin.TabularInline):
    model = Lesson

class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", 'author', 'title', 'time', 'is_active' )
    inlines = [ChapterInline]

class ChapterAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "title", "time", 'is_active' )
    inlines = [LessonInline]
    
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "title", "time", 'is_active' )
    
admin.site.register(Course, CourseAdmin)        
admin.site.register(Chapter, ChapterAdmin)        
admin.site.register(Lesson, LessonAdmin)        