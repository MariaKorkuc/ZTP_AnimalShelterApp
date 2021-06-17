# Generated by Django 3.2.3 on 2021-06-12 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AnimalShelterApp', '0003_alter_animal_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='reservedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='animals', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='animal',
            name='type',
            field=models.CharField(default='cat', max_length=20),
        ),
    ]
