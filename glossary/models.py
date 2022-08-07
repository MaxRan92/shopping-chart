from django.db import models
from algos.models import Category

# Create your models here.


class Terms(models.Model):

    class Meta:
        verbose_name_plural = 'Terms'
        ordering = ['term'] 

    term = models.CharField(max_length=254)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.term