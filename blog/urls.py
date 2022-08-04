from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_blog, name='view_blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
