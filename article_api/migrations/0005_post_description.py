# Generated by Django 4.0.2 on 2022-03-11 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_api', '0004_remove_post_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default='Description not available'),
            preserve_default=False,
        ),
    ]
