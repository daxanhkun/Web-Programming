# Generated by Django 2.2.14 on 2022-12-08 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20221208_0531'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialty',
            name='slug',
            field=models.SlugField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]
