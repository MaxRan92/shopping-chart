from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_algos, name='algos'),
    path('algo_id', views.algo_detail, name='algo_detail'),
]
