# Generated by Django 3.2.3 on 2021-06-11 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnimalShelterApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='image',
            field=models.CharField(default='', max_length=100),
        ),
    ]