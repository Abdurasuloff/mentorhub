from django.urls import path
from .views import SignupView, CustomUserUpdateView, ProfileView

urlpatterns = [
    path('signup', SignupView.as_view(), name='signup'),
    path('update_profile', CustomUserUpdateView.as_view(), name='update'),
    path('profile/<str:username>', ProfileView.as_view(), name='profile' )
]

