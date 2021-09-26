from django.views.generic import TemplateView


# Site Top
class IndexView(TemplateView):
    template_name = 'templates/index.html'


# Sign up
class SignUpView(TemplateView):
    template_name = 'templates/signup.html'


# Username/Password Reset
class ResetView(TemplateView):
    template_name = 'templates/reset.html'
