from django.db import models


class Terms(models.Model):

    term = models.CharField(max_length=254)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Terms'
        ordering = ['term']

    def __str__(self):
        return self.term
