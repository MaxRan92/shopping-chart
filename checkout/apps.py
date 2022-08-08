"""
Credits: the code is inspired and adapted from the
Code Institute Boutique Ado Project
"""
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
