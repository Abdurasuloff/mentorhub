from django.urls import path
from .views import NewCourseView, newChapter, CourseDashboardView, UpdateCourseView, DeleteCourseView
from .views import DeleteChapterView, DetailChapterView, DetailLessonView, NewLessonView, EditLessonView, DeleteLessonView
from .views import LandingPageView

app_name = 'course'
urlpatterns = [
    #courses
    path('new', NewCourseView.as_view(), name='new'),
    path('<int:id>/dashboard', CourseDashboardView.as_view(), name='dashboard'),
    path('<int:id>/update', UpdateCourseView.as_view(), name='update'),
    path('<int:id>/delete', DeleteCourseView.as_view(), name='delete'),
    #chapter
    path('new-chapter', newChapter, name='new-chapter'),
    path('chapter/<int:id>/detail', DetailChapterView.as_view(), name='detail-chapter'),
    path('chapter/<int:id>/delete', DeleteChapterView.as_view(), name='delete-chapter'),
    #lesson
    path('lesson/<int:id>/detail', DetailLessonView.as_view(), name='detail-lesson'),
    path('lesson/<int:chapter_id>/new', NewLessonView.as_view(), name='new-lesson'),
    path('lesson/<int:id>/edit', EditLessonView.as_view(), name='edit-lesson'),
    path('lesson/<int:id>/delete', DeleteLessonView.as_view(), name='delete-lesson'),
    #student
    path('<uuid:uuid>/landing-page', LandingPageView.as_view(), name="landing-page")
]