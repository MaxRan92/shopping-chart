"""
Credits: the code is inspired and adapted from the
Code Institute Boutique Ado Project
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_algos, name='algos'),
    path('<int:algo_id>/', views.algo_detail, name='algo_detail'),
    path('add/', views.add_algo, name='add_algo'),
    path('edit/<int:algo_id>/', views.edit_algo, name='edit_algo'),
    path('delete/<int:algo_id>/', views.delete_algo, name='delete_algo'),
]
