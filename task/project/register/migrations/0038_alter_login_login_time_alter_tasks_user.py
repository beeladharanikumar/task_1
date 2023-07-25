# Generated by Django 4.2.3 on 2023-07-20 10:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0037_alter_login_login_time_alter_tasks_task_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 20, 16, 18, 1, 374231)),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register.register'),
        ),
    ]
