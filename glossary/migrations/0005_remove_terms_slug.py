# Generated by Django 3.2 on 2022-08-07 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0004_alter_terms_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='terms',
            name='slug',
        ),
    ]
