from django.urls import path
from . import views


urlpatterns = [
    path('tools', views.get_tools, name='get_tools')
]
