from django.db import models

# Create your models here.

class normal_user(models.Model):
    user_no = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    nickname = models.CharField(max_length=12)
    phone_no = models.CharField(max_length=11)
    email = models.EmailField()
    security_question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
