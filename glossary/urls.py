from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_glossary, name='view_terms'),
    path('<int:pk>/delete_term/',
         views.TermDelete.as_view(), name="delete_term"),
    path('<int:pk>/edit_term/',
         views.TermEdit.as_view(), name="edit_term"),
]
