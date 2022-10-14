from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.main, name='main'),
    path('accounts/signup', views.signup, name='signup'),
]