# Generated by Django 2.1.4 on 2019-01-03 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.URLField(default='localhost:8000'),
        ),
    ]
