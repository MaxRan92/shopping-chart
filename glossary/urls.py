from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_glossary, name='view_terms'),
    path('<int:pk>/delete_comment/',
         views.TermDelete.as_view(), name="delete_term"),
]