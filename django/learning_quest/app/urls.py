from django.urls import path
from .views import IndexView, ResetView, TopView, signup_function
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(template_name='templates/login.html'), name='login'),
    path('signup/', signup_function, name='signup'),
    path('reset/', ResetView.as_view(), name='reset'),
    path('top/', TopView.as_view(), name='top'),
]