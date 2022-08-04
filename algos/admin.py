from django.contrib import admin
from .models import Algo, Category

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
