from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin


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
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('top')
    else:
        form = UserCreationForm()

    return render(request, 'templates/signup.html', {'form': form})


# logout
def logout_function(request):
    logout(request)
    return render(request, 'templates/login.html')


# Username/Password Reset
class TopView(LoginRequiredMixin, TemplateView):
    template_name = 'templates/topview.html'


# Username/Password Reset
class ResetView(TemplateView):
    template_name = 'templates/reset.html'
