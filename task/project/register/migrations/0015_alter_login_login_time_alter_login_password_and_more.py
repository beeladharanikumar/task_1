# Generated by Django 4.2.3 on 2023-07-17 05:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0014_alter_login_login_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 17, 11, 14, 51, 706440)),
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='user_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
