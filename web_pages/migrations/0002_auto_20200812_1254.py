# Generated by Django 3.0.8 on 2020-08-12 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
