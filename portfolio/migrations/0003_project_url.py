# Generated by Django 2.2.6 on 2019-11-18 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20191007_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True, max_length=250),
        ),
    ]
