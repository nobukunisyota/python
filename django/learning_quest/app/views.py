from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView


# Site Top
class IndexView(TemplateView):
    template_name = 'templates/index.html'


# Login
class Login(LoginView):
    template_name = 'templates/login.html'


# Sign up
class SignUpView(TemplateView):
    template_name = 'templates/signup.html'


# Username/Password Reset
class ResetView(TemplateView):
    template_name = 'templates/reset.html'
