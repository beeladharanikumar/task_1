# Generated by Django 4.2.3 on 2023-07-26 04:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0040_alter_file_upload_file_time_alter_login_login_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_upload',
            name='file_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 26, 10, 22, 36, 816387)),
        ),
        migrations.AlterField(
            model_name='login',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 26, 10, 22, 36, 814434)),
        ),
    ]