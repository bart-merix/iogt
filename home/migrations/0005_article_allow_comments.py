# Generated by Django 3.1.11 on 2021-06-01 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210409_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='allow_comments',
            field=models.BooleanField(default=True),
        ),
    ]
