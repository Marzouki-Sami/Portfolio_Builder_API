# Generated by Django 4.1.2 on 2022-11-27 16:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio_app', '0004_rename_discrition_certifications_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awards_honors',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 11, 27, 16, 32, 53, 556570, tzinfo=datetime.timezone.utc)),
        ),
    ]