from django.views.generic import TemplateView


# Site Top
class IndexView(TemplateView):
    template_name = 'templates/index.html'


# Login
class LoginView(TemplateView):
    template_name = 'templates/login.html'


# Sign up
class SignUpView(TemplateView):
    template_name = 'templates/signup.html'
