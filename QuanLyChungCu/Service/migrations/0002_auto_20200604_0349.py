# Generated by Django 3.0.6 on 2020-06-04 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='coefficient',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='service',
            name='note',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]