# Generated by Django 2.1.5 on 2019-02-14 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0003_participant_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='team',
        ),
    ]
