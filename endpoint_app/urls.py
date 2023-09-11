from django.urls import path
from . import views

app_name = 'app_name'
urlpatterns = [
    path('api', views.get_info, name='get_info'),
]
