from django.urls import path
from .views import IndexView, SignUpView, ResetView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(template_name='templates/login.html'), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('reset/', ResetView.as_view(), name='reset'),
    path('top/', ResetView.as_view(), name='top'),
]