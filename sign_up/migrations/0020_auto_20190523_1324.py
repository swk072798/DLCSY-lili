# Generated by Django 2.1.5 on 2019-05-23 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0019_auto_20190523_0934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competition_topic',
            old_name='max_upload_times',
            new_name='TestA_max_upload_times',
        ),
        migrations.AddField(
            model_name='competition_topic',
            name='TestB_max_upload_times',
            field=models.IntegerField(default='0'),
        ),
    ]