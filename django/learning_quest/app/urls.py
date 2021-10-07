from django.urls import path
from .views import IndexView, ResetView, TopView, SettingView , signup_function, logout_function
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(template_name='templates/login.html'), name='login'),
    path('logout/', logout_function, name='logout'),
    path('signup/', signup_function, name='signup'),
    path('reset/', ResetView.as_view(), name='reset'),
    path('top/', TopView.as_view(), name='top'),
    path('setting/', SettingView.as_view(), name='setting'),
]