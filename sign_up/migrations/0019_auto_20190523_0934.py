# Generated by Django 2.1.5 on 2019-05-23 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0018_auto_20190523_0926'),
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