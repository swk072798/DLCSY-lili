# Generated by Django 2.1.5 on 2019-05-23 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0017_auto_20190523_0925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition_topic',
            name='TestA_open_time',
        ),
        migrations.RemoveField(
            model_name='competition_topic',
            name='TestB_open_time',
        ),
    ]