from django.db import models
from algos.models import Category

# Create your models here.


class Terms(models.Model):

    term = models.CharField(max_length=254)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Terms'
        ordering = ['term'] 

    def __str__(self):
        return self.term