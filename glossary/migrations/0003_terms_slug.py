# Generated by Django 3.2 on 2022-08-07 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0002_alter_terms_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='terms',
            name='slug',
            field=models.SlugField(default='testslug', max_length=200, unique=True),
        ),
    ]
