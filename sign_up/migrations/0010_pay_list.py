# Generated by Django 2.1.5 on 2019-05-04 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('sign_up', '0009_auto_20190502_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='pay_list',
            fields=[
                ('list_id', models.AutoField(primary_key=True, serialize=False)),
                ('pay_money', models.IntegerField()),
                ('set_date', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.normal_user')),
            ],
        ),
    ]
