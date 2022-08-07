from django.db import models

# Create your models here.


class Newsletter(models.Model):

    class Meta:
        verbose_name_plural = 'Subscribers'

    email = models.EmailField(null=False, blank=False)
    privacy = models.BooleanField(null=False, blank=False)
