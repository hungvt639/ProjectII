# Generated by Django 3.0.6 on 2020-06-25 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notification', '0004_auto_20200513_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='notify',
            name='file',
            field=models.TextField(blank=True, null=True),
        ),
    ]
