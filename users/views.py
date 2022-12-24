from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import CustomUser
from django.contrib import messages

# Create your views here.
class SignupView(View):
    def get(self, request):
        create_form = CustomUserCreationForm()
        context = {
            "form": create_form
        }
        return render(request, "registration/signup.html", context)

    def post(self, request):
        create_form = CustomUserCreationForm(data=request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect('login')
        else:
            context = {
                "form": create_form
            }
            return render(request, "registration/signup.html", context)
        
class CustomUserUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        user_update_form = CustomUserUpdateForm(instance=request.user)
        return render(request, "registration/profile_update.html", {"form": user_update_form})

    def post(self, request):
        user_update_form = CustomUserUpdateForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES
        )

        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request, "You have successfully updated your profile.")

            return redirect("profile", request.user.username)

        return render(request, "registration/profile_update.html", {"form": user_update_form})        
    
    
class ProfileView(View, LoginRequiredMixin):
    def get(self, request, username):
        user = CustomUser.objects.get(username=username)
        context = {
            'profile_user':user,
            }        
        return render(request, 'registration/profile.html', context)    