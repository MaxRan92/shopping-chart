"""
Credits: the code is inspired and adapted from the
Code Institute Boutique Ado Project
"""
from django.contrib import admin
from .models import Algo, Category


# Register your models here.
class AlgoAdmin(admin.ModelAdmin):
    """
    Set the admin panel for Algo model
    """
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
    """
    Set the admin panel for category model
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Algo, AlgoAdmin)
admin.site.register(Category, CategoryAdmin)
