# Generated by Django 2.2.4 on 2022-06-19 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0004_auto_20220619_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='description',
            field=models.TextField(default='There is no descriptipn'),
        ),
        migrations.DeleteModel(
            name='Description',
        ),
    ]
