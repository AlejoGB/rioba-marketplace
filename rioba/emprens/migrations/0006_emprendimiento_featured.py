# Generated by Django 3.1 on 2020-08-25 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprens', '0005_emprendimiento_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprendimiento',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
