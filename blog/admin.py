from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''
    Add the comment models to the admin panel
    apply summernote to the comment text field
    add approved/not approved filters and serach
    functionalities
    '''
    list_display = ('name', 'body', 'post',
                    'created_on', 'user_rating',)
    list_filter = ('created_on',)
    search_fields = ('name', 'email', 'body')
