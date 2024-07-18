from django.urls import path
from . import views

urlpatterns = [
    path('', views.regex_query, name='regex_query'),
]
