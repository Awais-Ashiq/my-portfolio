# Generated by Django 3.0.4 on 2020-03-30 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
