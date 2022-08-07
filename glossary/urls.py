from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_glossary, name='view_terms'),
]