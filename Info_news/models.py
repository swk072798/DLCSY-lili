from django.db import models

# Create your models here.

class article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    ar_time = models.DateField()
    type = models.CharField(max_length=5,default='')

class study_resource(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    type = models.CharField(max_length=4)

class system_info(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("login.normal_user",on_delete=models.CASCADE)
    info_content = models.CharField(max_length=200)
    now_date = models.DateTimeField(auto_now_add=True)
