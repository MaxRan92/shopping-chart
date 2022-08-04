from django.contrib import admin
from .models import Algo, Category, Comment

# Register your models here.
class AlgoAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )
    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Algo, AlgoAdmin)
admin.site.register(Category, CategoryAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''
    Add the comment models to the admin panel
    apply summernote to the comment text field
    add approved/not approved filters and serach
    functionalities
    '''
    list_display = ('name', 'body', 'algo',
                    'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'body',)
