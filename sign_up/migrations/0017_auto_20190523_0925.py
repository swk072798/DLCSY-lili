# Generated by Django 2.1.5 on 2019-05-23 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0016_competition_topic_money_to_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition_topic',
            name='TestA_open_time',
            field=models.DateField(default='2019-1-1'),
        ),
        migrations.AlterField(
            model_name='competition_topic',
            name='TestB_open_time',
            field=models.DateField(default='2019-1-1'),
        ),
    ]
