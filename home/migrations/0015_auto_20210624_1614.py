# Generated by Django 3.1.12 on 2021-06-24 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_merge_20210624_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.DeleteModel(
            name='ArticleTag',
        ),
    ]
