# Generated by Django 2.2.4 on 2022-06-14 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ninjas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('dojo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ninja', to='dojo_ninjas_app.dojos')),
            ],
        ),
    ]
