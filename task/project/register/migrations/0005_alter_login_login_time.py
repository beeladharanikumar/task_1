# Generated by Django 4.2.3 on 2023-07-14 04:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_alter_login_login_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 14, 9, 57, 55, 228440)),
        ),
    ]
