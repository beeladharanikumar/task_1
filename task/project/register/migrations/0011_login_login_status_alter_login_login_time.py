# Generated by Django 4.2.3 on 2023-07-14 05:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_alter_login_login_time_alter_login_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='login_status',
            field=models.CharField(default='register', max_length=30),
        ),
        migrations.AlterField(
            model_name='login',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 14, 11, 9, 14, 163427)),
        ),
    ]
