# Generated by Django 2.2.4 on 2022-06-19 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0005_auto_20220619_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='description',
            field=models.TextField(default='There is no description'),
        ),
    ]