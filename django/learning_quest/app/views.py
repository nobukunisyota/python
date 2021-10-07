from django.views.generic import TemplateView, ListView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import RewardTable, StudyTime


# Site Top
class IndexView(TemplateView):
    template_name = 'templates/index.html'


# Sign up
def signup_function(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'templates/topview.html', {'user': user})
    else:
        form = UserCreationForm()

    return render(request, 'templates/signup.html', {'form': form})


# logout
def logout_function(request):
    logout(request)
    return render(request, 'templates/login.html')


# Main View
class TopView(LoginRequiredMixin, ListView):
    template_name = 'templates/topview.html'
    model = RewardTable

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'study_time': StudyTime.objects.all()
        })
        return context

    def get_queryset(self):
        return RewardTable.objects.all()


class SettingView(ListView):
    template_name = 'templates/setting.html'
    model = RewardTable

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'study_time': StudyTime.objects.all()
        })
        return context

    def get_queryset(self):
        return RewardTable.objects.all()


# Username/Password Reset
class ResetView(TemplateView):
    template_name = 'templates/reset.html'
