# Generated by Django 2.1.5 on 2019-05-23 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0011_competition_topic_max_upload_times'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition_topic',
            name='TestA_open_time',
            field=models.DateField(default='2019-01-01'),
        ),
        migrations.AddField(
            model_name='competition_topic',
            name='TestB_open_time',
            field=models.DateField(default='2019-01-01'),
        ),
    ]
