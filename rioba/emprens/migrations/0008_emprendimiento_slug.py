# Generated by Django 3.1 on 2020-08-25 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprens', '0007_emprendimiento_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprendimiento',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
