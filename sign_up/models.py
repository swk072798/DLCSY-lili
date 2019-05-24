from django.db import models


# Create your models here.

class competition_topic(models.Model):
    com_topic_id = models.AutoField(primary_key=True)
    com_name = models.CharField(max_length=20)
    com_details = models.TextField()
    com_end_time = models.DateField()
    data_set_file_trainnig = models.CharField(max_length=100,default='')
    data_set_file_A = models.CharField(max_length=100, default='')
    data_set_file_B = models.CharField(max_length=100, default='')
    TestA_max_upload_times = models.IntegerField(default="0")
    TestB_max_upload_times = models.IntegerField(default="0")
    TestA_open_time = models.DateField(default='2019-01-01')
    TestB_open_time = models.DateField(default='2019-01-01')
    money_to_pay = models.IntegerField(default='500')

class participant(models.Model):
    user = models.OneToOneField("login.normal_user",on_delete=models.CASCADE)
    real_name = models.CharField(max_length=10)
    sex = models.CharField(max_length=2)
    id_num = models.CharField(max_length=18)
    address = models.CharField(max_length=50)
    event = models.ForeignKey("competition_topic",on_delete=models.CASCADE)
    team = models.ForeignKey("join_team.team_info",on_delete=models.CASCADE,default='',null=True)

class address_details(models.Model):
    user_id = models.OneToOneField("login.normal_user",on_delete=models.CASCADE,primary_key=True)
    address = models.CharField(max_length=100)

class pay_list(models.Model):
    list_id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField("login.normal_user",on_delete=models.CASCADE)
    pay_money = models.IntegerField()
    set_date = models.DateTimeField(auto_now_add=True)