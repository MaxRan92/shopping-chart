from django.contrib import admin
from .models import Terms


@admin.register(Terms)
class TermsAdmin(admin.ModelAdmin):
    list_display = ('term', 'description',)
    prepopulated_fields = {'slug': ('term',)}
    search_fields = ['term',]
