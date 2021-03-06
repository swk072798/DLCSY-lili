# Generated by Django 2.1.5 on 2019-02-14 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='normal_user',
            fields=[
                ('user_no', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=12)),
                ('phone_no', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('security_question', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=255)),
            ],
        ),
    ]
