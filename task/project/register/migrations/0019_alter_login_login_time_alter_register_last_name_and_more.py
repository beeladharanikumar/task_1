# Generated by Django 4.2.2 on 2023-07-17 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0018_alter_login_login_time_alter_register_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 17, 18, 50, 38, 159992)),
        ),
        migrations.AlterField(
            model_name='register',
            name='last_name',
            field=models.CharField(default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='phone_number',
            field=models.CharField(default='', max_length=12, null=True),
        ),
    ]