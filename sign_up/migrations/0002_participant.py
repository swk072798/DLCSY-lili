# Generated by Django 2.1.5 on 2019-02-14 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('sign_up', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_name', models.CharField(max_length=10)),
                ('sex', models.CharField(max_length=2)),
                ('id_num', models.CharField(max_length=18)),
                ('address', models.CharField(max_length=50)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sign_up.competition_topic')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.normal_user')),
            ],
        ),
    ]
