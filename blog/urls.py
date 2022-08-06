from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_blog, name='view_blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/<int:pk>/delete_comment/',
         views.CommentDelete.as_view(), name="delete_comment"),
    path('<slug:slug>/<int:pk>/edit_comment/',
         views.CommentEdit.as_view(), name="edit_comment"),
]
