# Generated by Django 2.1.5 on 2019-02-14 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sign_up', '0002_participant'),
    ]

    operations = [
        migrations.CreateModel(
            name='team_info',
            fields=[
                ('team_no', models.AutoField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=50, null=True)),
                ('num_of_troops', models.IntegerField(null=True)),
                ('captain', models.CharField(max_length=10, null=True)),
                ('person_info', models.ManyToManyField(to='sign_up.participant')),
                ('team_event', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='sign_up.competition_topic')),
            ],
        ),
    ]
