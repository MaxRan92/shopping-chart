from django.contrib import admin
from .models import Enquiry


class EnquiryAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'first_name',
        'last_name',
        'email',
        'title',
        'body',
    )

    ordering = ('date',)


admin.site.register(Enquiry, EnquiryAdmin)