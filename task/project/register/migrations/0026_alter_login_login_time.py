# Generated by Django 4.2.3 on 2023-07-18 06:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0025_alter_login_login_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 18, 11, 30, 6, 993866)),
        ),
    ]