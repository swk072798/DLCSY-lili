from django.db import models

# Create your models here.

class video(models.Model):
    id = models.AutoField(primary_key=True)
    video_topic = models.CharField(max_length=50)
    video_urls = models.CharField(max_length=100)
    video_type = models.CharField(max_length=20,default="")