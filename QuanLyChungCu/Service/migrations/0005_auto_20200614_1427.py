# Generated by Django 3.0.6 on 2020-06-14 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0004_auto_20200608_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_using',
            name='time_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]