from django.shortcuts import render, redirect
from .models import Course, Chapter, Lesson
from .forms import CourseForm, ChapterForm, LessonForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

class NewCourseView(View, LoginRequiredMixin):
    def get(self, request ):
        if request.user.is_teacher == True:
            context = {"form": CourseForm()}
            return render(request, "courses/new.html", context)
        else:
            messages.error(request, "You do not have a permission!")
            return redirect("index")
    def post(self, request):
        course_form = CourseForm(data=request.POST)
        if course_form.is_valid():
            course_form.instance.author = request.user
            course_form.save()
            messages.success(request, "Base course is successfully created!")
            return redirect('index')

class CourseDashboardView(View, LoginRequiredMixin):
    def get(self, request, id):
        course = get_object_or_404(Course, id=id, author=request.user)
        context = {
            "course":course,
        }
        return render(request, 'courses/dashboard.html', context)
    
class UpdateCourseView(View, LoginRequiredMixin):
    def get(self, request, id):
        course = get_object_or_404(Course, id=id, author = request.user)
        course_form = CourseForm(instance=course)
        return render(request, 'courses/edit.html', {"form": course_form})    
    
    def post(self, request, id):
        course = get_object_or_404(Course, id=id, author = request.user)
        course_form = CourseForm(instance=course, data=request.POST, files=request.FILES)
        
        if course_form.is_valid():
            course_form.save()
            return redirect('course:dashboard', course.id)
            messages.success(request, "Successfully changed")
        else:    
            return render(request, 'courses/edit.html', {"form": course_form})

class DeleteCourseView(View, LoginRequiredMixin):
    def get(self, request, id):
        course = get_object_or_404(Course, id=id, author = request.user)
        course.delete()
        messages.success(request, "Successfully deleted")
        return redirect('main:index')

@login_required
def newChapter(request):
    if request.method == "POST":
        course = Course.objects.get(id=request['course_id'])
        Chapter.objects.create(
            course = course,
            author = request.user,
            title = request.POST['title']
        )     
        messages.success(request, "Chapter is successfully created!")
        return redirect('course:dashboard', course.id )                  

class DetailChapterView(View, LoginRequiredMixin):
    def get(self, request, id):
        chapter = get_object_or_404(Chapter, id=id, author=request.user)
        chapter_form = ChapterForm(instance=chapter)
        
        context = {
            "form":chapter_form,
        }
        return render(request, 'courses/chapter_detail.html',  context)
    
    def post(self, request, id):
        chapter = get_object_or_404(Chapter, id=id, author = request.user)
        chapter_form = ChapterForm(instance=chapter, data=request.POST)
        
        if chapter_form.is_valid():
            chapter_form.save()
            messages.success(request, "Successfully changed.")
            return redirect("course:detail-chapter", chapter.id)
        else:
            context = {
                "form":chapter_form,
            }
            return render(request, 'courses/chapter_detail.html',  context)
        
class DeleteChapterView(View, LoginRequiredMixin):
    def get(self, request, id):
        chapter = get_object_or_404(Chapter, id=id, author=request.user)
        chapter.delete()
        messages.success(request, "Chapter is successfully deleted.")
        return redirect("course:dashboard")
                
class DetailLessonView(View, LoginRequiredMixin):
    def get(self, request, id):
        lesson  = get_object_or_404(Lesson, id=id, author=request.user)       
        context = {
            'lesson':lesson,
        }
        return render(request, 'courses/lesson_detail.html', context)         

class NewLessonView(View, LoginRequiredMixin):
    def get(self, request, chapter_id):
        chapter = get_object_or_404(Chapter, id=chapter_id, author=request.user)
        return render(request, 'courses/lesson_new.html', {"form": LessonForm(), "chapter":chapter})    
    
    def post(self, request, chapter_id):
        chapter = get_object_or_404(Chapter, id=chapter_id, author=request.user)
        lesson_form = LessonForm(data=request.POST)
        if lesson_form.is_valid():
            lesson_form.instance.chapter = chapter
            lesson_form.instance.author = request.user
            lesson_form.save()
            messages.success(request, "Successfully created!")
            return redirect("course:detail-chapter", chapter.id)
        else:
            return render(request, 'courses/lesson_new.html', {"form": lesson_form, "chapter":chapter})
            
class EditLessonView(View, LoginRequiredMixin):
    def get(self, request, id):
        lesson = get_object_or_404(Lesson, id=id, author=request.user)
        lesson_form = LessonForm(instance=lesson)
        context = {
            'lesson':lesson,
            "form":lesson_form,
        }
        return render(request, 'courses/lesson_edit.html', context)
    
    def post(self, request, id):
        lesson = get_object_or_404(Lesson, id=id, author=request.user)
        lesson_form = LessonForm(instance=lesson, data=request.POST)
        if lesson_form.is_valid():
            lesson_form.save()
            messages.success(request, "Successfully updated!")
            return redirect("course:detail-lesson", lesson.id)
        else:
                context = {
                    'lesson':lesson,
                    "form":lesson_form,
                } 
                return render(request, 'courses/lesson_edit.html', context) 

class DeleteLessonView(View, LoginRequiredMixin):
    def get(self, request, id):
        lesson = get_object_or_404(Lesson, id=id, author=request.user)
        lesson.delete()
        messages.success(request, "Lesson is successfully deleted ")            
        return redirect('course:detail-chapter', lesson.chapter.id)
    
class LandingPageView(View, LoginRequiredMixin):
    def get(self, request, uuid):
        course = get_object_or_404(Course, slug=uuid)
        context = {
             "course": course,
        }
        return render(request, "courses/landing_page.html", context)   
    