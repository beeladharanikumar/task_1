# Generated by Django 4.2.3 on 2023-07-17 05:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0015_alter_login_login_time_alter_login_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 17, 11, 20, 44, 583699)),
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='user_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
