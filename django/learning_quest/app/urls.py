from django.urls import path
from .views import IndexView, Login, SignUpView, ResetView

urlpatterns = [
    path('', IndexView.as_view(), name='app:index'),
    path('login/', Login.as_view(), name='app:login'),
    path('signup/', SignUpView.as_view(), name='app:signup'),
    path('reset/', ResetView.as_view(), name='app:reset'),
    path('top/', ResetView.as_view(), name='app:top'),
]