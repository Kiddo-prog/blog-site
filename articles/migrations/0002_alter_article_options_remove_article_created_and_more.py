# Generated by Django 4.0 on 2022-04-10 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={},
        ),
        migrations.RemoveField(
            model_name='article',
            name='created',
        ),
        migrations.RemoveField(
            model_name='article',
            name='updated',
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='hello.jpg', max_length=100, null=True, unique=True),
        ),
    ]
