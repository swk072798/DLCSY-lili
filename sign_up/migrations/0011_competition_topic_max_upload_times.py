# Generated by Django 2.1.5 on 2019-05-23 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0010_pay_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition_topic',
            name='max_upload_times',
            field=models.IntegerField(default='0'),
        ),
    ]